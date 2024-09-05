'use client'
import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

import { Perk } from "@/types/matchTypes";

export default function PerkIconCSR({ perk, perkID, size }: { perk: Perk; perkID: number; size: number }) {

  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
        <TooltipTrigger>
          <Image
            src={`http://localhost:8000/static/dragontail-14.15.1/perk-images-byID/perk-images/Styles/${perkID}.png`}
            className="m-0.5"
            width={size}
            height={size}
            alt={`Item ${perkID}`}
          />
        </TooltipTrigger>
        <TooltipContent className="bg-slate-700 bg-opacity-90 backdrop-blur-md rounded-[20px] border-2 w-80">
          <p className="font-bold text-amber-600">{perk.name}</p>
          <p>{perk.description}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>    
  );
}
