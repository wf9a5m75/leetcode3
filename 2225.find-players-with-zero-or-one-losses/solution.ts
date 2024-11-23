function findWinners(matches: number[][]): number[][] {
  const numsOfLostMap = new Map<number, number>();
  
  const players = new Set<number>();
  for (const [winner, loser] of matches) {
      players.add(winner);
      players.add(loser);
      numsOfLostMap.set(loser, (numsOfLostMap.get(loser) || 0) + 1);
  }
  
  const allWinPlayers: number[] = [];
  const lostOneMatchPlayers: number[] = [];
  for (const player of players.values()) {
      if (!numsOfLostMap.has(player)) {
          allWinPlayers.push(player);
          continue;
      }
      if (numsOfLostMap.get(player) === 1) {
          lostOneMatchPlayers.push(player);
      }
  }
  allWinPlayers.sort((a, b) => a - b);
  lostOneMatchPlayers.sort((a, b) => a - b);
  return [allWinPlayers, lostOneMatchPlayers];
};
