import { formatDistanceToNowStrict } from 'date-fns';

export function relativeTime(date: Date | number): string {
  return formatDistanceToNowStrict(date, { addSuffix: true });
}