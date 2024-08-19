import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip"
import parse from 'html-react-parser'
import ItemDescription from "./ItemDescription";

import { fetchItems } from "@/api/datadragon";

const ItemIcon = async ({ itemID, size }: { itemID: number; size: number }) => {
  const items = await fetchItems();
  const item = items[itemID]
  if (itemID === 0) {
    return (
      <div className="w-6 h-6 m-0.5 border border-white bg-white bg-opacity-20 backdrop-blur-md"></div>
    );
  }
  return (
    <TooltipProvider>
      <Tooltip delayDuration={200}>
        <TooltipTrigger>
          <Image
            src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/item/${itemID}.png`}
            className="m-0.5"
            width={size}
            height={size}
            alt={`Item ${itemID}`}
          />
        </TooltipTrigger>
        <TooltipContent className="bg-slate-700 bg-opacity-90 backdrop-blur-md rounded-[20px] border-2 w-80">
          <p className="font-bold">{item.name}</p>
          <ItemDescription description={item.description} />
          {item.gold.total === 0 ? (<p></p>) : (        
            <div className="flex">
              <div>Cost: </div>
              <div className="text-amber-600 ml-1">{item.gold.total}</div>
            </div>)}
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}

export default ItemIcon;
