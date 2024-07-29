"use client";
import React, { useState } from "react";

import { useRouter } from 'next/navigation'

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { MatchData } from '@/types/matchTypes';

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
});

interface FormData {
  username: string;
  region: string;
}

interface Match {
  win: boolean;
  championId: number;
  championName: string;
  invidualPosition: string;
  teamId: number;
}

interface ProfileFormProps {
  setMatchHistory: React.Dispatch<React.SetStateAction<Match[]|null>>;
}

const regions = ["NA", "EUW", "EUNE", "KR", "BR", "JP", "OCE"];

export function ProfileForm({setMatchHistory}: ProfileFormProps) {
  const router = useRouter()

  const handleSubmit = async (formData: FormData) => {
    try {
      const response = await fetch(`http://localhost:8000/match_history?nickname=${formData.username}&tag=${formData.region}`);
      setMatchHistory(await response.json())
      router.push(`/user?summonername=${formData.username}&tag=${formData.region}`)
    } catch (error) {
      console.error('Error fetching match data:', error);
    }
  };

  const [selectedRegion, setSelectedRegion] = useState(regions[0]);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
    },
  });

  function onSubmit(values: z.infer<typeof formSchema>) {
    const formData = { ...values, region: selectedRegion };
    console.log(formData);
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
            <DropdownMenuContent className="bg-white bg-opacity-20 backdrop-blur-md border-2 border-white border-opacity-30 rounded-md overflow-hidden">
              {regions.map((region) => (
                <DropdownMenuItem
                  key={region}
                  onSelect={() => setSelectedRegion(region)}
                  className="text-white hover:bg-white hover:bg-opacity-30 transition-colors duration-300 focus:bg-white focus:bg-opacity-30 focus:text-black"
                >
                  {region}
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
                  <div className="relative">
                    <Input
                      placeholder="Summoner name + Tag"
                      {...field}
                      className="w-full py-3 pl-5 pr-12 text-lg text-white bg-white bg-opacity-20 backdrop-blur-md rounded-r-full border-2 border-white border-opacity-30 focus:border-opacity-60 focus:outline-none focus:ring-2 focus:ring-white focus:ring-opacity-30 transition-all duration-300 placeholder-gray-300"
                      onKeyDown={(e) => {
                        if (e.key === "Enter") {
                          e.preventDefault();
                          const searchButton =
                            document.getElementById("searchButton");
                          searchButton?.classList.add("active");
                          setTimeout(() => {
                            searchButton?.classList.remove("active");
                          }, 150);
                          form.handleSubmit(onSubmit)();
                        }
                      }}
                    />
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
