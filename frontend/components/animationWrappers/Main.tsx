"use client";

import { motion, AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";

const variants = {
  hidden: { x: "100%", opacity: 0 },
  enter: { x: 0, opacity: 1 },
  exit: { x: "-100%", opacity: 0 },
};

export default function MainAnimationWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const pathname = usePathname();
  const shouldAnimate = pathname.startsWith("/summoner");

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
