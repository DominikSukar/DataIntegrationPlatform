import Link from "next/link";

import { Participant, Info } from "@/types/matchTypes";

import ChampionIcon from "./ChampionIcon";
import SpellIcon from "./SpellIcon";
import RankIcon from "./RankIcon";

const GameDetailsParticipant = async ({
  participant,
  info,
}: {
  participant: Participant;
  info: Info;
}) => {
  return (
    <div className="flex">
      <ChampionIcon championName={participant.championName} size={20}></ChampionIcon>
      {/* ChampionIconCOLUMN: tooltip to show leveling */}
      <div className="flex flex-col">
            {participant.summoners.map((summoner, index) => (
              <SpellIcon spellID={summoner} size={8} key={index} />
            ))}
      </div>
      {/* PerksColumn */}
      {/* TOPERKSCOLUMN: tooltip to show perks specifics */}
      <RankIcon rankName="Emerald" size={20}></RankIcon>
      <Link
        href={`/summoner/${info.server}/${participant.summonerName}_${participant.tagLine}`}
        className="no-underline"
      >
        <h6
          className={`w-16 xl:w-28 text-left overflow-hidden whitespace-nowrap text-ellipsis text-slate-400 hover:text-slate-500 transition-colors duration-200 ease-in-out ${
            participant.isMain ? "font-bold text-white" : ""
          }`}
        >
          {participant.summonerName}#{participant.tagLine}
        </h6>
      </Link>
      <h6 className="flex flex-col items-center justify-center">
        <h6 className="flex justify-center">
          {participant.kills}
          {<h6 className="text-slate-400">/</h6>}
          {
            <h6 className="text-red-600 font-bold">
              {participant.deaths}
            </h6>
          }
          {<h6 className="text-slate-400">/</h6>}
          {participant.assists}
        </h6>
        <div className="flex">
          <h6
            className={`
          ${
            participant.kda < 1.0
              ? "text-red-500"
              : participant.kda < 3.0
              ? "text-white-400"
              : participant.kda < 5.0
              ? "text-green-400"
              : participant.kda < 10.0
              ? "text-blue-400"
              : "text-yellow-500"
          }`}
          >
            {participant.kda}
          </h6>
          <h6 className="ml-1 text-gray-400">KDA</h6>
        </div>
      </h6>
      {/* KP */}
      {/* CS + CS/min */}
      {participant.vision}
      {/* DPS + Obj DPS */}
      {/* DPS Taken */}
      {/* Gold */}
      {/* Items */}
      {/* Button to show item buying order */}
    </div>
  );
};

export default GameDetailsParticipant;
