import Link from "next/link";

import { Participant, Info } from "@/types/matchTypes";

import ChampionIcon from "./ChampionIcon";
import SpellIconCSR from "./SpellIconCSR";
import RankIcon from "./RankIcon";
import PerkIcon from "./PerkIcon";

const GameDetailsParticipant = ({
  participant,
  info,
  isReversed,
}: {
  participant: Participant;
  info: Info;
  isReversed?: boolean;
}) => {
  const primaryPerks = participant.perks.primary;
  const secondaryPerks = participant.perks.secondary;

  return (
    <div
      className={`flex items-center ${isReversed ? "flex-row-reverse" : ""}`}
    >
      <ChampionIcon
        championName={participant.championName}
        size={36}
      ></ChampionIcon>
      {/* ChampionIconCOLUMN: tooltip to show leveling */}
      <div className="flex flex-col">
        {participant.summoners.map((summoner, index) => (
          <SpellIconCSR spellID={summoner} size={16} key={index} />
        ))}
      </div>
      <div className="flex flex-col">
        <PerkIcon perkID={primaryPerks.perks[0]} size={16}></PerkIcon>
        <PerkIcon perkID={secondaryPerks.style} size={16}></PerkIcon>
      </div>
      {/* TOPERKSCOLUMN: tooltip to show perks specifics */}
      <RankIcon rankName="Emerald" size={36}></RankIcon>
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
      <div className="flex flex-col items-center justify-center w-20">
        <div className="flex justify-center">
          <h6>{participant.kills}</h6>
          <h6 className="text-slate-400">/</h6>
          <h6 className="text-red-600 font-bold">{participant.deaths}</h6>
          <h6 className="text-slate-400">/</h6>
          <h6>{participant.assists}</h6>
        </div>
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
      </div>
      <div className="flex">
            <h6
              className={`
          ${
            participant.kp < 40
              ? "text-red-500"
              : participant.kp < 60
              ? "text-white-400"
              : participant.kp < 80
              ? "text-green-400"
              : participant.kp < 90
              ? "text-blue-400"
              : "text-yellow-500"
          }`}
            >
              {participant.kp}
            </h6>
            <h6 className="text-gray-400">% KP</h6>
          </div>
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
