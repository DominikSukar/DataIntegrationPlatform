import Image from "next/image";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import ItemDescription from "./ItemDescription";

import { Item, ItemCollection } from "@/types/matchTypes";

import { DOMAIN } from "../../constants/api";

export default async function ItemIcon({
  itemID,
  size,
}: {
  itemID: number;
  size: number;
}) {
  const response = await fetch(`${DOMAIN}/datadragon/items/`, {
    next: { revalidate: 3600 },
  });
  const items: ItemCollection = await response.json();
  const item: Item = items[itemID];

  if (itemID === 0) {
    return (
      <div
        className={
          "w-6 h-6 m-0.5 border border-slate-400 bg-white bg-opacity-20 backdrop-blur-md"
        }
      ></div>
    );
  }
  /* https://blog.ggboost.com/bl-content/uploads/pages/731fd39180a3f7570690918001c01fa4/lol-new-items-confusion-1.webp
  Dodac :after do css, aby wyswietlal te podstawowe ikonki. Zmienic kolorystke - wypierdolic wszystko, aktywy na ciemny pomaranczowy.
   */

  return (
    <TooltipProvider>
      <Tooltip delayDuration={200} disableHoverableContent={true}>
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
          <div className="flex p-2">
            <Image
              src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/item/${itemID}.png`}
              className="m-0.5 mr-6 h-14"
              width={56}
              height={56}
              alt={`Item ${itemID}`}
            />
            <div>
              <p className="font-bold text-amber-600">{item.name}</p>
              <ItemDescription description={item.description} />
              {item.gold.total === 0 ? (
                <p></p>
              ) : (
                <div className="flex">
                  <div>Cost: </div>
                  <div className="text-amber-600 ml-1">{item.gold.total}</div>
                </div>
              )}
            </div>
          </div>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
}
