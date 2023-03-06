import styles from './home-view.module.scss';
import { clsx } from 'clsx';
import { useState, useEffect } from 'react';
import {
  ExtPowerButton,
  StrengthSlider,
  NeumorphicSwitch,
  NeumorphicSetting,
} from '@athena-vision/shared/ui';
import { FILTER_BUTTONS } from '@athena-vision/shared/const-values';
import { useStateContext } from '../fetch-context/fetch-context';

// const chrome = window.chrome;

/* eslint-disable-next-line */
export interface HomeViewProps {}

export function HomeView(props: HomeViewProps) {
  const [strengthState, setStrengthState] = useState('1');
  const [filterBtn, setFilterBtn] = useState(FILTER_BUTTONS);
  const [settingView, setSettingView] = useState(false);
  const [extState, setExtState] = useState(false);
  const [initialRender, setInitialRender] = useState(true);

  const { mutateFilter, mutatePredictor, extPowerData } = useStateContext();

  useEffect(() => {
    if (!initialRender) {
      if (extPowerData.extOn) {
        setFilterBtn((prev) => ({ ...prev, blur: extPowerData.blur }));
        setStrengthState(extPowerData.strength);
      } else {
        const { strength, extOn, ...others } = extPowerData;
        setFilterBtn((prev) => ({ ...others }));
        setStrengthState(strength);
      }
    }
  }, [extPowerData?.extOn]);


  useEffect(() => {
    const fectData = async () => {
      if (!initialRender) {
        try {
          await mutatePredictor(extState);
        } catch (error) {
          console.log(error);
        }
        console.log('mutating predictor btn');
      }
    };

    fectData();
  }, [extState]);

  useEffect(() => {
    if (!initialRender && extState) {
      const data = {
        ...filterBtn,
        strength: strengthState,
      };
      mutateFilter(data);
      console.log('mutating filter btn');
    }
    setInitialRender(false);
  }, [
    strengthState,
    filterBtn['blur'],
    filterBtn['emotional tone'],
    filterBtn['topic label'],
  ]);

  useEffect(() => {
    const opt = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': true,
        'X-Requested-With': 'XMLHttpRequest',
      },
      mode: 'cors',
    };

    fetch('http://127.0.0.1:8000/athena/setting/', opt)
      .then((res) => res.json())
      .then((data) => {
        console.log(data)
        const { strength, ...other } = data;
        setStrengthState((_) => strength);
        setFilterBtn((_) => ({ ...other }));
      });
  }, []);

  return (
    <div
      className={styles['container']}
      data-setting-active={settingView ? 'active' : 'off'}
    >
      <div>
        {/* Enable button */}
        <div
          className={clsx(
            styles['d-flex'],
            styles['flex-center'],
            styles['full-screen']
          )}
        >
          {/* Button to turn Extension on/off */}
          <ExtPowerButton extState={extState} setExtState={setExtState} />
          {/* Filters */}
          <div className={styles['settings']}>
            <NeumorphicSetting
              active={settingView}
              setActive={setSettingView}
            />

            <div className={styles['filter-form']}>
              <StrengthSlider
                strengthState={strengthState}
                setStrengthState={setStrengthState}
              />
              {Object.entries(filterBtn).map(([key, value]) => (
                <NeumorphicSwitch
                  filterTitle={key}
                  checked={value}
                  setChecked={setFilterBtn}
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomeView;
