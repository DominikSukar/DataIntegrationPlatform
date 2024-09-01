"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";

import { DOMAIN } from "../../constants/api";

const SpellIconCSR = ({ spellID, size }: { spellID: number; size: number }) => {
  const [summoner, setSummoner] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`${DOMAIN}/datadragon/summoners/`);
      const summoners = await response.json();
      setSummoner(summoners[spellID]);
      setLoading(false);
      console.log(summoners, summoner)
    };

    fetchData();
  }, []);

  if (loading) return <></>;

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
          <p className="font-bold text-amber-600">{summoner ? (summoner.name) : (<></>)}</p>
          <p>{summoner ? (summoner.description) : (<></>)}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
};

export default SpellIconCSR;
