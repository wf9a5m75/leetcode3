function checkIfPangram(sentence: string): boolean {
  const existences = Array(26).fill(false);
  const codeA = "a".charCodeAt(0);
  let offset = 0;
  for (let i = 0; i < sentence.length; i++) {
      offset = sentence.charCodeAt(i) - codeA;
      existences[offset] = true;
  }
  for (let i = 0; i < existences.length; i++) {
      if (!existences[i]) {
          return false;
      }
  }
  return true;
};
