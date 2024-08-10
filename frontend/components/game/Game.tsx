import React from "react";

import { secondsToHMS } from "../../utils/time";

import MatchParticipant from "./MatchParticipant";

import ChampionIcon from "./ChampionIcon";
import SpellIcon from "./SpellIcon";
import ItemIcon from "./ItemIcon";

import { Participant, MatchData } from "@/types/matchTypes";

function Game({ match }: { match: MatchData }) {
  const gameClasses = {
    win: "border-indigo-700",
    lose: "border-red-700",
  };

  const mainParticipant = match.main_participant;
  const team_1 = match.team_1;
  const team_2 = match.team_2;
  const info = match.info;

  return (
    <div
      className={`bg-white bg-opacity-20 backdrop-blur-md rounded-l-full border-4 
         rounded-[10px] m-1 p-2 px-5 w-fit flex items-center justify-around gap-5 min-w-[700px]
          ${gameClasses[mainParticipant.win ? "win" : "lose"]}
          animate-fadeInUp`}
    >
      <div className="flex">
        <div className="flex flex-col items-center justify-center m-1 min-w-16">
          <h3>{mainParticipant.win ? "Victory" : "Defeat"}</h3>
          <div>{mainParticipant.individualPosition}</div>
          <p>{secondsToHMS(mainParticipant.timePlayed)}</p>
        </div>
        <div className="flex flex-col">
          <div className="flex items-center justify-center m-1 min-w-16">
            <ChampionIcon championName={mainParticipant.championName} size={70}></ChampionIcon>
            <div>
              {mainParticipant.summoners.map((summoner, index)=>(
                <SpellIcon spellID={summoner} size={34} key={index}/>
              ))}
            </div>
          </div>
          <div className="flex">
            {mainParticipant.items.map((item, index)=>(
              <ItemIcon itemID={item} size={24} key={index}/>
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
          <div className={`
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
          }`}>{mainParticipant.kda} KDA</div>
        </div>
      </div>
      <div className="min-w-[400px] flex justify-center">
        <div>
          {team_1.map((participant, index) => (
            <MatchParticipant
              key={index}
              participant={participant}
              info={info}
            />
          ))}
        </div>
        <div>
          {team_2.map((participant, index) => (
            <MatchParticipant
              key={index}
              participant={participant}
              info={info}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Game;
