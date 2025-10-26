import React, { useEffect, useRef } from "react";

const ClockGrid = () => {
  const canvasRef = useRef(null);
  const rows = 7; // number of rows
  const cols = 23; // number of columns
  const clockSize = 30; // pixel size of each clock
  const spacing = 4;

  // Create digit patterns using 7x5 grids
  const DIGITS = {
    0: ["11111", "10001", "10011", "10101", "11001", "10001", "11111"],
    1: ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    2: ["11111", "00001", "00001", "11111", "10000", "10000", "11111"],
    3: ["11111", "00001", "00001", "11111", "00001", "00001", "11111"],
    4: ["10001", "10001", "10001", "11111", "00001", "00001", "00001"],
    5: ["11111", "10000", "10000", "11111", "00001", "00001", "11111"],
    6: ["11111", "10000", "10000", "11111", "10001", "10001", "11111"],
    7: ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    8: ["11111", "10001", "10001", "11111", "10001", "10001", "11111"],
    9: ["11111", "10001", "10001", "11111", "00001", "00001", "11111"],
    ":": ["00000", "00100", "00100", "00000", "00100", "00100", "00000"],
  };

  // Draw clock hands for each cell
  const drawClock = (ctx, x, y, active) => {
    ctx.beginPath();
    ctx.arc(x, y, clockSize / 2, 0, Math.PI * 2);
    ctx.strokeStyle = "rgba(100,100,100,0.3)";
    ctx.lineWidth = 1;
    ctx.stroke();

    if (active) {
      // active cell -> highlight with L shape
      ctx.strokeStyle = "#ccff33";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x - clockSize / 3, y - clockSize / 3);
      ctx.lineTo(x - clockSize / 3, y + clockSize / 3);
      ctx.lineTo(x + clockSize / 3, y + clockSize / 3);
      ctx.stroke();
    }
  };

  const drawTime = (ctx, timeString) => {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    const chars = timeString.split("");
    let offsetX = 0;

    chars.forEach((char) => {
      const pattern = DIGITS[char];
      if (!pattern) return;
      pattern.forEach((row, r) => {
        row.split("").forEach((c, col) => {
          const x = offsetX + col * (clockSize + spacing);
          const y = r * (clockSize + spacing);
          drawClock(ctx, x, y, c === "1");
        });
      });
      offsetX += 6 * (clockSize + spacing); // space between digits
    });
  };

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    const updateClock = () => {
      const now = new Date();
      const time = now
        .toLocaleTimeString("en-US", { hour12: false })
        .slice(0, 5); // HH:MM
      drawTime(ctx, time);
    };

    updateClock();
    const interval = setInterval(updateClock, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <canvas
      ref={canvasRef}
      width={cols * (clockSize + spacing)}
      height={rows * (clockSize + spacing)}
      className="bg-black mx-auto my-8 block"
    />
  );
};

export default ClockGrid;
