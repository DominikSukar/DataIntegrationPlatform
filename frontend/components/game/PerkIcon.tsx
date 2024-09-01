import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"

const PerkIcon = async({ perkID, size }: { perkID: number; size: number }) => {
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
      </Tooltip>
    </TooltipProvider>    
  );
}

export default PerkIcon;
