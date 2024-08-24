import MatchParticipant from "./MatchParticipant";
import { Participant, Info } from "@/types/matchTypes";

function GameParticipants({
  team_1,
  team_2,
  info,
}: {
  team_1: Participant[];
  team_2: Participant[];
  info: Info;
}) {
  return (
    <div className="flex justify-center items-center invisible w-0 xl:visible xl:w-max">
      <div>
        {team_1.map((participant, index) => (
          <MatchParticipant key={index} participant={participant} info={info} />
        ))}
      </div>
      <div>
        {team_2.map((participant, index) => (
          <MatchParticipant key={index} participant={participant} info={info} />
        ))}
      </div>
    </div>
  );
}

export default GameParticipants;
