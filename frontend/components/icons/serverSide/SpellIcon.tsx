import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

import { Spell, SpellCollection } from "@/types/matchTypes";
import { DOMAIN } from "@/constants/api";

export default async function SpellIcon({ spellID, size }: { spellID: number; size: number }) {
  const response = await fetch(`${DOMAIN}/datadragon/summoners/`, {
    next: { revalidate: 3600 },
  });
  const summoners: SpellCollection = await response.json()
  const summoner: Spell = summoners[spellID]
  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
        <TooltipTrigger>
          <Image
            src={`${DOMAIN}/static/dragontail-14.15.1/14.15.1/img/spell/${spellID}.png`}
            className="m-0.5"
            width={size}
            height={size}
            alt={`Item ${spellID}`}
          />
        </TooltipTrigger>
        <TooltipContent className="bg-slate-700 bg-opacity-90 backdrop-blur-md rounded-[20px] border-2 w-80">
          <p className="font-bold text-amber-600">{summoner.name}</p>
          <p>{summoner.description}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>    
  );
}
