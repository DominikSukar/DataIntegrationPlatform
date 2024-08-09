import Link from "next/link";
import ChampionIcon from "../components/ChampionIcon";

import { Participant, Info } from "@/types/matchTypes";

function MatchParticipant({
  participant,
  info,
}: {
  participant: Participant;
  info: Info;
}) {
  if (participant.teamId === 100) {
    return (
      <div className="flex font-light text-xs justify-end items-center">
        <Link
          href={`/summoner/${info.server}/${participant.summonerName}_${participant.tagLine}`}
          className="no-underline"
        >
          <div className="w-28 text-right overflow-hidden whitespace-nowrap text-ellipsis text-white">
            {participant.summonerName}#{participant.tagLine}
          </div>
        </Link>
        <ChampionIcon championName={participant.championName}></ChampionIcon>
        <div
          className={`w-16 flex justify-center items-center
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
        </div>
      </div>
    );
  }

  return (
    <div className="flex font-light text-xs justify-start items-center">
      <div
        className={`w-16 flex justify-center items-center
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
      </div>
      <ChampionIcon championName={participant.championName}></ChampionIcon>
      <Link
        href={`/summoner/${participant.server}/${participant.summonerName}_${participant.tagLine}`}
        className="no-underline"
      >
        <div className="w-28 text-left overflow-hidden whitespace-nowrap text-ellipsis text-white">
          {participant.summonerName}#{participant.tagLine}
        </div>
      </Link>
    </div>
  );
}

export default MatchParticipant;
