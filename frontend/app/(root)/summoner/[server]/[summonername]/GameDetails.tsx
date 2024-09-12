"use client";
import { Transition } from "@headlessui/react";
import { useState, useEffect } from "react";
import GameDetailsParticipant from "./GameDetailsParticipant";

import { Button } from "@/components/ui/button";

import { Participant, Info } from "@/types/matchTypes";

import { IPSContextProvider } from "@/contexts/IPSContext";

export default function GameDetails({
  team_1,
  team_2,
  info,
}: {
  team_1: Participant[];
  team_2: Participant[];
  info: Info;
}) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <IPSContextProvider>
      <div className="flex flex-col items-center">
        <Button
          className="w-20 border border-white bg-white bg-opacity-5 backdrop-blur-md"
          onClick={() => setIsOpen(!isOpen)}
        >
          Details
        </Button>
        <Transition
          show={isOpen}
          enter="transition-all duration-700 ease-out"
          enterFrom="opacity-0 max-h-0 overflow-hidden"
          enterTo="opacity-100 max-h-[1000px]"
          leave="transition-all duration-700 ease-out"
          leaveFrom="opacity-100 max-h-[1000px]"
          leaveTo="opacity-0 max-h-0 overflow-hidden"
        >
          <div className="flex justify-center gap-20 transition duration-600 ease-in-out">
            <div>
              <h2 className="text-center text-red-500">Red team</h2>
              {team_1.map((participant, index) => (
                <GameDetailsParticipant
                  key={index}
                  participant={participant}
                  info={info}
                />
              ))}
              {/*Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS */}
            </div>
            <div>
              {/* Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS */}
              <h2 className="text-center text-blue-500">Blue team</h2>
              {team_2.map((participant, index) => (
                <GameDetailsParticipant
                  key={index}
                  participant={participant}
                  info={info}
                  isReversed={true}
                />
              ))}
            </div>
          </div>
        </Transition>
      </div>
    </IPSContextProvider>
  );
}
