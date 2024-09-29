"use client";
import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

import { Perk } from "@/types/matchTypes";
import { PERK_URL } from "@/constants/api";

export default function PerkIconCSR({
  perk,
  perkID,
  size,
}: {
  perk: Perk;
  perkID: number;
  size: number;
}) {
  console.log(perk)
  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
        <TooltipTrigger>
          <Image
            src={`${PERK_URL}/${perkID}.png`}
            className="m-0.5"
            width={size}
            height={size}
            alt={`Item ${perkID}`}
          />
        </TooltipTrigger>
        <TooltipContent className="bg-slate-700 bg-opacity-90 backdrop-blur-md rounded-[20px] border-2 w-80">
          <p className="font-bold text-amber-600">{perk? (perk.name) : (<></>)}</p>
          <p>{perk? (perk.description) : (<></>)}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}
