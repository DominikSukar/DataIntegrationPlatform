import { MainParticipant, Info } from "@/types/matchTypes";
import { relativeTime } from "@/utils/relativeDate";
import { secondsToHMS } from "@/utils/time";

function GameInfo({
  mainParticipant,
  info,
}: {
  mainParticipant: MainParticipant;
  info: Info;
}) {
  const gameDate = new Date(info.gameEndTimestamp);
  return (
    <div className="flex flex-col items-center justify-center m-1 lg:min-w-36">
      <h3
        className={`${
          info.gameResult === 'Win' ? "text-indigo-300" : info.gameResult === 'Defeat' ? "text-red-300" : "text-slate-400"
        } `}
      >
        {info.gameResult}
      </h3>
      <div>{secondsToHMS(mainParticipant.timePlayed)}</div>
      <div className="text-center">{relativeTime(gameDate)}</div>
      <div className="text-sm text-slate-400 w-0 invisible xl:visible xl:w-max">{info.matchId}</div>
    </div>
  );
}

export default GameInfo;
