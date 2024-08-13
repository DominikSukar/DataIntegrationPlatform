import { MainParticipant, Info } from "@/types/matchTypes";
import { secondsToHMS } from "@/utils/time";

function GameInfo({
  mainParticipant,
  info,
}: {
  mainParticipant: MainParticipant;
  info: Info;
}) {
  const gameDate = new Date(info.gameEndTimestamp).toDateString();
  return (
    <div className="flex flex-col items-center justify-center m-1 min-w-16">
      <h3
        className={`${
          mainParticipant.win ? "text-indigo-300" : "text-red-300"
        } `}
      >
        {mainParticipant.win ? "Victory" : "Defeat"}
      </h3>
      <div>{secondsToHMS(mainParticipant.timePlayed)}</div>
      <div>{gameDate}</div>
    </div>
  );
}

export default GameInfo;
