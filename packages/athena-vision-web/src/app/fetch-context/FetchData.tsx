import { useState, createContext, useContext } from 'react';
import { OPT } from '@athena-vision/shared/const-values';
import { IFilterButton } from '@athena-vision/shared/typedefs';

const StateContext = createContext(null);

interface IFilterData extends IFilterButton {
  strength: '0' | '1' | '2';
}

const StateContextProvider = ({ children }) => {
  const mutateFilter = async (filterData: IFilterData) => {
    try {
      const opt: any = {
        ...OPT,
        method: 'POST',
        body: JSON.stringify(filterData),
      };

      const _ = await fetch('http://127.0.0.1:8000/athena/mutateBlur/', opt);
      console.log('successful blur mutated');
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <StateContext.Provider
      value={{
        mutateFilter,
      }}
    >
      {children}
    </StateContext.Provider>
  );
};

export const useStateContext = () => useContext(StateContext);
