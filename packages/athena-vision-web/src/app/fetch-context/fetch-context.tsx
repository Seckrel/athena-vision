import { useState, createContext, useContext } from 'react';
import { OPT } from '@athena-vision/shared/const-values';
import { IFilterButton } from '@athena-vision/shared/typedefs';

const StateContext = createContext(null);

interface IFilterData extends IFilterButton {
  strength: '0' | '1' | '2';
}

interface IExtResponse {
  blur?: number;
  status?: number;
  extOn: boolean;
}

export const StateContextProvider = ({ children }) => {
  const [extPowerData, setExtPowerData] = useState<IExtResponse>({
    extOn: false
  });
  const mutateFilter = async (filterData: IFilterData) => {
    try {
      const opt: any = {
        ...OPT,
        method: 'POST',
        body: JSON.stringify(filterData),
      };

      const _ = await fetch('http://127.0.0.1:8000/athena/setting/', opt);
      console.log('successful blur mutated');
    } catch (error) {
      console.log(error);
    }
  };

  const mutatePredictor = async (extSate: boolean) => {
    try {
      const opt = {
        ...OPT,
        method: 'POST',
        body: JSON.stringify(extSate),
      };
      const response = await fetch(
        'http://127.0.0.1:8000/athena/extPower/',
        opt
      );
      const data = await response.json();

      if (data.extOn) {
        setExtPowerData({ blur: data.blur, extOn: true, strength: data.strength });
      } else {
        setExtPowerData((_) => ({ ...data, extOn: false }));
      }
      console.log('successful ext power');
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <StateContext.Provider
      value={{
        mutateFilter,
        mutatePredictor,
        extPowerData,
      }}
    >
      {children}
    </StateContext.Provider>
  );
};

export const useStateContext = () => useContext(StateContext);
