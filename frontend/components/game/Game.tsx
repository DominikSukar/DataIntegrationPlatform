import GameInfo from "./GameInfo";
import GameParticipants from "./GameParticipants";
import GameMainParticipant from "./GameMainParticipant";

import { MatchData } from "@/types/matchTypes";

function Game({ match }: { match: MatchData }) {
  const gameClasses = {
    win: "border-indigo-700",
    lose: "border-red-700",
  };

  const mainParticipant = match.main_participant;

  return (
    <div
      className={`bg-white bg-opacity-20 backdrop-blur-md rounded-l-full border-4 
         rounded-[10px] m-1 p-2 px-5 w-fit flex items-center justify-around gap-5 min-w-[700px]
          ${gameClasses[mainParticipant.win ? "win" : "lose"]}
          animate-fadeInUp`}
    >
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
  );
}

export default Game;
