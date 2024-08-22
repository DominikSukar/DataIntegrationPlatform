"use client";

import { motion, AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";

const variants = {
  hidden: { opacity: 0, y: 50, scale: 0.7 },
  enter: { opacity: 1, y: 0, scale: 1 },
  exit: { opacity: 0, y: -50, scale: 0.7 },
};

export default function SummonersAnimationWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const shouldAnimate = pathname.startsWith("/summoner");
  console.log(pathname, shouldAnimate);

  return (
    <AnimatePresence mode="wait">
      {shouldAnimate ? (
        <motion.main
          key={pathname}
          variants={variants}
          initial="hidden"
          animate="enter"
          exit="exit"
          transition={{ type: "linear" }}
        >
          {children}
        </motion.main>
      ) : (
        children
      )}
    </AnimatePresence>
  );
}
