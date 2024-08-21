import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import ItemDescription from "./ItemDescription";

import { fetchSummoners } from "@/api/datadragon";

const SpellIcon = async({ spellID, size }: { spellID: number; size: number }) => {
  const summoners = await fetchSummoners();
  const summoner = summoners[spellID]
  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
        <TooltipTrigger>
          <Image
            src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/spell/${spellID}.png`}
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

export default SpellIcon;
