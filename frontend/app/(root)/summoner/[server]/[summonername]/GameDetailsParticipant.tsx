import Link from "next/link";

import { Participant, Info, ItemCollection, PerkCollection, SpellCollection } from "@/types/matchTypes";

import ChampionIcon from "@/components/icons/serverSide/ChampionIcon";
import SpellIconCSR from "@/components/icons/clientSide/SpellIconCSR";
import RankIcon from "@/components/icons/serverSide/RankIcon";
import PerkIconCSR from "@/components/icons/clientSide/PerkIconCSR";
import ItemIconCSR from "@/components/icons/clientSide/ItemIconCSR";

export default function GameDetailsParticipant({
  participant,
  info,
  items,
  perks,
  spells,
  isReversed,
}: {
  participant: Participant;
  info: Info;
  items: ItemCollection;
  perks: PerkCollection;
  spells: SpellCollection;
  isReversed?: boolean;
}) {
  const primaryPerks = participant.perks.primary;
  const secondaryPerks = participant.perks.secondary;

  return (
    <div
      className={`flex my-1 items-center ${
        !isReversed ? "flex-row-reverse" : ""
      }`}
    >
      <div>
        <div>
          <div className="flex justify-center">
            <ChampionIcon
              championName={participant.championName}
              size={40}
            ></ChampionIcon>
            {/* ChampionIconCOLUMN: tooltip to show leveling */}
            <div className="flex flex-col">
              {participant.summoners.map((spellID, index) => (
                <SpellIconCSR spell={spells[spellID]} spellID={spellID} size={20} key={index} />
              ))}
            </div>
            <div className="flex flex-col">
              <PerkIconCSR
                perk={perks[primaryPerks.perks[0]]}
                perkID={primaryPerks.perks[0]}
                size={20}
              ></PerkIconCSR>
              <PerkIconCSR
                perk={perks[secondaryPerks.style]}
                perkID={secondaryPerks.style}
                size={20}
              ></PerkIconCSR>
            </div>
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
            <div className="flex items-center">
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
          </div>
          <div className="flex">
            {participant.items.map((itemID, index) => (
              <ItemIconCSR item={items[itemID]} itemID={itemID} size={24} key={index} />
            ))}
          </div>
        </div>
      </div>
      {/* TOPERKSCOLUMN: tooltip to show perks specifics */}
      <div className="flex flex-col items-center mx-5">
        <Link
          href={`/summoner/${info.server}/${participant.summonerName}_${participant.tagLine}`}
          className="no-underline"
        >
          <h6
            className={`w-16 xl:w-28 text-center overflow-hidden whitespace-nowrap text-ellipsis text-slate-400 hover:text-slate-500 transition-colors duration-200 ease-in-out ${
              participant.isMain ? "font-bold text-white" : ""
            }`}
          >
            {participant.summonerName}#{participant.tagLine}
          </h6>
        </Link>
        <div className="flex">
          <RankIcon rankName="Emerald" size={20}></RankIcon>
          <h6 className="text-slate-400">Emerald 3</h6>
        </div>
      </div>

      {/* CS + CS/min */}
      {participant.vision}
      {/* DPS + Obj DPS */}
      {/* DPS Taken */}
      {/* Gold */}
      {/* Button to show item buying order */}
    </div>
  );
};
