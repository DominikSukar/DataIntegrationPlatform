import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

/* Component is used on both client and server side. Do not put async.*/
export default function ChampionIcon({
  championName,
  size,
}: {
  championName: string;
  size: number;
}) {
  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
        <TooltipTrigger>
          <Image
            src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/champion/${championName}.png`}
            className="m-0.5"
            width={size}
            height={size}
            alt={`Champion ${championName}`}
          />
        </TooltipTrigger>
        <TooltipContent className="bg-slate-700 bg-opacity-90 backdrop-blur-md rounded-full border-2">
          <p className="font-bold text-amber-600">{championName}</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}
