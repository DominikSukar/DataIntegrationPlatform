export interface MatchParticipant {
    win: boolean;
    championId: number;
    championName: string;
    individualPosition: string;
    teamId: number;
  }
  
  export interface MatchData extends Array<MatchParticipant | { time: number; time_before_fetching: number }> {}