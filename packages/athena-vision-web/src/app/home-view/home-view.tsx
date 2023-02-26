import styles from './home-view.module.scss';
import { clsx } from 'clsx';
import { useState } from 'react';
import {
  ExtPowerButton,
  StrengthSlider,
  NeumorphicSwitch,
  NeumorphicSetting,
} from '@athena-vision/shared/ui';
import { FILTER_BUTTONS } from '@athena-vision/shared/const-values';

/* eslint-disable-next-line */
export interface HomeViewProps {}

export function HomeView(props: HomeViewProps) {
  const [strengthState, setStrengthState] = useState('1');
  const [filterBtn, setFilterBtn] = useState(FILTER_BUTTONS);
  const [settingView, setSettingView] = useState(false);

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
          <ExtPowerButton />
          {/* Filters */}
          <div className={styles['settings']}>
            <NeumorphicSetting
              active={settingView}
              setActive={setSettingView}
            />

            <div className={styles["filter-form"]}>
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
