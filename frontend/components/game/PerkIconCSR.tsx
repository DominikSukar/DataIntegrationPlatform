'use client'
import Image from "next/image";
import { useEffect, useState } from "react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

import { DOMAIN } from "../../constants/api";

const PerkIconCSR = ({ perkID, size }: { perkID: number; size: number }) => {
  const [perk, setPerk] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`${DOMAIN}/datadragon/perks/`);
      const perks = await response.json();
      setPerk(perks[perkID]);
      setLoading(false);
    };

    fetchData();
  }, []);

  if (loading) return <></>;

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

export default PerkIconCSR;
