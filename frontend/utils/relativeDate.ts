import { formatDistanceToNow } from 'date-fns';

export function relativeTime(date: Date | number): string {
  return formatDistanceToNow(date, { addSuffix: true });
}