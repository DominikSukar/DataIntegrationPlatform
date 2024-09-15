import { z } from "zod";
import { formSchema } from "@/constants/userSearch";

export interface IFormData {
    username: string;
    region: string;
}

export type FormValues = z.infer<typeof formSchema>;