function* inorderTraversal(arr) {
  for (const el of arr) {
    if (Array.isArray(el)) {
      yield* inorderTraversal(el);
    } else {
      yield el;
    }
  }
}
