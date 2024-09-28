import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

import { Perk, PerkCollection } from "@/types/matchTypes";
import { DOMAIN } from "@/constants/api";

export default async function PerkIcon({
  perkID,
  size,
}: {
  perkID: number;
  size: number;
}) {
  const response = await fetch(`${DOMAIN}/datadragon/perks/`, {
    next: { revalidate: 3600 },
  });
  const perks: PerkCollection = await response.json();
  const perk: Perk = perks[perkID];

  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
        <TooltipTrigger>
          <Image
            src={`${DOMAIN}/static/dragontail-14.15.1/perk-images-byID/perk-images/Styles/${perkID}.png`}
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
