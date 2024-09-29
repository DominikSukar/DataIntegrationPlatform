"use client";
import React, { useState, useEffect, useRef } from "react";
import Cookies from "js-cookie";
import { Transition } from "@headlessui/react";

import { useRouter } from "next/navigation";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

import { IFormData } from "@/types/userSearch";
import { formSchema } from "@/constants/userSearch";
import { DOMAIN } from "@/constants/api";
import { defaultRegions } from "@/constants/userSearch";

export default function UserSearch() {
  const router = useRouter();
  const [regions, setRegion] = useState(defaultRegions);
  const [selectedRegion, setSelectedRegion] = useState("EUW");
  const [searchedSummoners, setSearchedSummoners] = useState([""]);
  const [isSummonersDropdownOpen, setIsSummonersDropdownOpen] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const fetchServers = async () => {
      const response = await fetch(`${DOMAIN}/server/`);
      const result = await response.json();
      setRegion(result);
    };
    fetchServers();
    const savedRegion = Cookies.get("selectedRegion");
    if (savedRegion && regions.some(region => region.symbol === savedRegion)) {
      setSelectedRegion(savedRegion);
    }
    const summonersCookie: string | undefined = Cookies.get("summonersSearch");
    if (summonersCookie) {
      const summoners: string[] = JSON.parse(summonersCookie);
      setSearchedSummoners(summoners);
    }
    const handleClickOutside = (event: MouseEvent) => {
      if (
        inputRef.current &&
        !inputRef.current.contains(event.target as Node)
      ) {
        setIsSummonersDropdownOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const handleRegionChange = (region: string) => {
    setSelectedRegion(region);
    Cookies.set("selectedRegion", region, { expires: 365 });
  };

  const handleSubmit = async (formData: IFormData) => {
    let userString = "";
    if (!formData.username.includes(formData.region)) {
      userString = `${formData.username}`;
    } else {
      userString = formData.username;
    }
    const searchEntry = userString;
    const summonersSearchCookie: string | undefined =
      Cookies.get("summonersSearch");

    if (summonersSearchCookie) {
      let summonersSearch: string[] = JSON.parse(summonersSearchCookie);
      // Summoner found in the cookie results in him being removed and then added at the beginning
      summonersSearch = summonersSearch.filter(
        (entry) => entry !== searchEntry
      );
      searchEntry.includes(formData.region);
      summonersSearch.unshift(searchEntry);

      summonersSearch = summonersSearch.slice(0, 10);
      Cookies.set("summonersSearch", JSON.stringify(summonersSearch), {
        expires: 365,
      });
    } else {
      Cookies.set("summonersSearch", JSON.stringify([searchEntry]), {
        expires: 365,
      });
    }
    router.push(`/summoner/${formData.region}/${formData.username}`);
  };

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
    },
  });

  function onSubmit(values: z.infer<typeof formSchema>) {
    const formData = { ...values, region: selectedRegion };
    handleSubmit(formData);
  }

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="w-full max-w-md mx-auto"
      >
        <div className="relative flex">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button
                variant="outline"
                className="mr-2 w-20 bg-white bg-opacity-20 backdrop-blur-md rounded-l-full border-2 border-white border-opacity-30 focus:border-opacity-60 text-white hover:bg-opacity-30 transition-all duration-300"
              >
                {selectedRegion} ▼
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="bg-white bg-opacity-20 backdrop-blur-md border-2 border-white border-opacity-30 rounded-md overflow-hidden max-h-[200px] overflow-y-auto">
              {regions.map((region) => (
                <DropdownMenuItem
                  key={region.symbol}
                  onSelect={() => handleRegionChange(region.symbol)}
                  className="text-white hover:bg-white hover:bg-opacity-30 transition-colors duration-300 focus:bg-white focus:bg-opacity-30 focus:text-black"
                >
                  {region.symbol}
                </DropdownMenuItem>
              ))}
            </DropdownMenuContent>
          </DropdownMenu>
          <FormField
            control={form.control}
            name="username"
            render={({ field }) => (
              <FormItem className="flex-grow mb-6">
                <FormControl>
                  <div className="relative" ref={inputRef}>
                    <Input
                      placeholder="Summoner name + Tag"
                      autoComplete="off"
                      {...field}
                      className="w-full py-3 pl-5 pr-12 text-lg text-white bg-white bg-opacity-20 backdrop-blur-md rounded-r-full border-2 border-white border-opacity-30 focus:border-opacity-60 focus:outline-none focus:ring-2 focus:ring-white focus:ring-opacity-30 transition-all duration-300 placeholder-gray-300"
                      onFocus={() => setIsSummonersDropdownOpen(true)}
                      onChange={(e) => {
                        field.onChange(e);
                        setIsSummonersDropdownOpen(true);
                      }}
                    />
                    <Transition
                      show={isSummonersDropdownOpen}
                      enter="transition-all duration-500 ease-in"
                      enterFrom="max-h-0 overflow-hidden"
                      enterTo="max-h-[1000px] overflow-hidden"
                      leave="transition-all duration-500 ease-out"
                      leaveFrom="max-h-[1000px] overflow-hidden"
                      leaveTo="max-h-0 overflow-hidden"
                    >
                      <div className="absolute z-10 w-full mt-1">
                        <ul className="bg-white bg-opacity-20 backdrop-blur-md border-2 border-white border-opacity-30 rounded-md overflow-hidden">
                          {searchedSummoners.map((summoner) => (
                            <li
                              key={summoner}
                              onClick={() => {
                                field.onChange(summoner);
                                setIsSummonersDropdownOpen(false);
                                handleSubmit({
                                  username: summoner,
                                  region: selectedRegion,
                                });
                              }}
                              className="px-4 py-2 text-white hover:bg-white hover:bg-opacity-30 transition-colors duration-300 cursor-pointer"
                            >
                              {summoner.replace("_", "#")}
                            </li>
                          ))}
                        </ul>
                      </div>
                    </Transition>
                    <button
                      id="searchButton"
                      type="submit"
                      className="absolute inset-y-0 right-0 flex items-center pr-3 transition-all duration-150 hover:opacity-80 active:transform active:scale-90"
                      onClick={() => {
                        const searchButton =
                          document.getElementById("searchButton");
                        searchButton?.classList.add("active");
                        setTimeout(() => {
                          searchButton?.classList.remove("active");
                        }, 150);
                      }}
                    >
                      <svg
                        className="w-6 h-6 text-white opacity-60"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                        ></path>
                      </svg>
                    </button>
                  </div>
                </FormControl>
                <FormMessage className="absolute mt-2 text-sm font-semibold px-2 py-1 rounded bg-red-500 text-white" />
              </FormItem>
            )}
          />
        </div>
      </form>
    </Form>
  );
}
