import ChampionIcon from "./ChampionIcon";
import SpellIcon from "./SpellIcon";
import ItemIcon from "./ItemIcon";

import { MainParticipant } from "@/types/matchTypes";

function GameMainParticipant({
  mainParticipant,
}: {
  mainParticipant: MainParticipant;
}) {
  return (
    <div className="flex items-center">
      <div className="flex flex-col">
        <div className="flex items-center justify-center m-1 min-w-16">
          <ChampionIcon
            championName={mainParticipant.championName}
            size={70}
          ></ChampionIcon>
          <div className="flex flex-col">
            {mainParticipant.summoners.map((summoner, index) => (
              <SpellIcon spellID={summoner} size={32} key={index} />
            ))}
          </div>
        </div>
        <div className="flex">
          {mainParticipant.items.map((item, index) => (
            <ItemIcon itemID={item} size={24} key={index} />
          ))}
        </div>
      </div>
      <div className="flex flex-col items-center justify-center m-10 min-w-16">
        <div className="flex justify-center min-w-16">
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
      </div>
    </div>
  );
}

export default GameMainParticipant;
