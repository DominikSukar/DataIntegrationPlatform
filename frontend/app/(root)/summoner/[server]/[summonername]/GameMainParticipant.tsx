import ChampionIcon from "@/components/icons/serverSide/ChampionIcon";
import SpellIcon from "@/components/icons/serverSide/SpellIcon";
import ItemIcon from "@/components/icons/serverSide/ItemIcon";
import PerkIcon from "@/components/icons/serverSide/PerkIcon";

import { MainParticipant } from "@/types/matchTypes";

export default function GameMainParticipant({
  mainParticipant,
}: {
  mainParticipant: MainParticipant;
}) {
  const primaryPerks = mainParticipant.perks.primary;
  const secondaryPerks = mainParticipant.perks.secondary;

  return (
    <div className="flex items-center  max-w-[330px]">
      <div className="flex flex-col">
        <div className="flex items-center justify-center m-1">
          <ChampionIcon
            championName={mainParticipant.championName}
            size={70}
          ></ChampionIcon>
          <div className="flex flex-col">
            {mainParticipant.summoners.map((summoner, index) => (
              <SpellIcon spellID={summoner} size={32} key={index} />
            ))}
          </div>
          {/*Hovering over perks should trigger animation that renders all the perks on (maybe) right side*/}
          <div className="flex flex-col">
            <PerkIcon perkID={primaryPerks.perks[0]} size={32}></PerkIcon>
            <PerkIcon perkID={secondaryPerks.style} size={32}></PerkIcon>
          </div>
        </div>
        <div className="flex">
          {mainParticipant.items.map((itemID, index) => (
            <ItemIcon itemID={itemID} size={24} key={index} />
          ))}
        </div>
      </div>
      <div className="flex flex-col items-center justify-center m-5 xl:m-10">
        <div className="flex justify-center">
          {mainParticipant.kills}
          {<span className="text-slate-400">/</span>}
          {
            <span className="text-red-600 font-bold">
              {mainParticipant.deaths}
            </span>
          }
          {<span className="text-slate-400">/</span>}
          {mainParticipant.assists}
        </div>
        <div className="flex">
          <div
            className={`
          ${
            mainParticipant.kda < 1.0
              ? "text-red-500"
              : mainParticipant.kda < 3.0
              ? "text-white-400"
              : mainParticipant.kda < 5.0
              ? "text-green-400"
              : mainParticipant.kda < 10.0
              ? "text-blue-400"
              : "text-yellow-500"
          }`}
          >
            {mainParticipant.kda}
          </div>
          <p className="ml-1 text-gray-400">KDA</p>
        </div>
        <div className="flex">
          <div
            className={`
          ${
            mainParticipant.kp < 40
              ? "text-red-500"
              : mainParticipant.kp < 60
              ? "text-white-400"
              : mainParticipant.kp < 80
              ? "text-green-400"
              : mainParticipant.kp < 90
              ? "text-blue-400"
              : "text-yellow-500"
          }`}
          >
            {mainParticipant.kp}
          </div>
          <p className="text-gray-400">% KP</p>
        </div>
      </div>
    </div>
  );
}
