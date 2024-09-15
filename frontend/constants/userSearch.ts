import { z } from "zod";

export const regions = ["NA", "EUW", "EUNE", "KR", "BR", "JP", "OCE"];

export const formSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
});