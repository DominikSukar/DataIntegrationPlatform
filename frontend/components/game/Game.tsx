import GameInfo from "./GameInfo";
import GameParticipants from "./GameParticipants";
import GameMainParticipant from "./GameMainParticipant";
import GameDetails from "./GameDetails";

import CSButton from "./CSButton";

import { MatchData, Result, Info } from "@/types/matchTypes";

function Game({ match}: { match: MatchData}) {
  const gameClasses: Record<Result, string> = {
    Win: "border-indigo-700",
    Defeat: "border-red-700",
    Remake: "border-slate-400",
  };

  const mainParticipant = match.main_participant;
  const gameResult = match.info.gameResult;

  return (
    <div
      className={`bg-white bg-opacity-20 backdrop-blur-md  border-4 xl:min-w-[925px]
         rounded-[10px] m-1 p-1 lg:px-5  
         ${gameClasses[gameResult]}
          animate-fadeInUp`}
    >
      <div className="flex items-center justify-around lg:gap-5">
        <GameInfo
          mainParticipant={match.main_participant}
          info={match.info}
        ></GameInfo>
        <GameMainParticipant
          mainParticipant={mainParticipant}
        ></GameMainParticipant>
        <GameParticipants
          team_1={match.team_1}
          team_2={match.team_2}
          info={match.info}
        ></GameParticipants>
      </div>
      <GameDetails
        team_1={match.team_1}
        team_2={match.team_2}
        info={match.info}
      ></GameDetails>
    </div>
  );
}

export default Game;
