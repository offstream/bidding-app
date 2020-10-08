import { useEffect, useState } from "react";

export const useFetch = url => {
  const [state, setState] = useState({ data: null, loading: true });

  useEffect(() => {
    setState(state => ({ data: state.data, loading: true }));
    fetch(url)
      .then(r => r.json())
      .then(d => {
        setState({ data: d, loading: false });
      });
  }, [url, setState]);

  return state;
};
