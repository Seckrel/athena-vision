import styles from './home-view.module.scss';
import { clsx } from 'clsx';
import { useState } from 'react';
import {
  ExtPowerButton,
  StrengthSlider,
  NeumorphicSwitch,
} from '@athena-vision/shared/ui';

/* eslint-disable-next-line */
export interface HomeViewProps {}

export function HomeView(props: HomeViewProps) {
  const [strengthState, setStrengthState] = useState('1');

  return (
    <div className={styles['container']}>
      {/* Enable button */}
      <div
        className={clsx(
          styles['d-flex'],
          styles['flex-center'],
          styles['full-screen']
        )}
      >
        {/* <button className={clsx(styles['enable-btn'], 'Typography-1')}>
          Enable
        </button> */}

        <ExtPowerButton />

        {/* Adjust Form */}
        <form>
          <StrengthSlider
            strengthState={strengthState}
            setStrengthState={setStrengthState}
          />
          <NeumorphicSwitch />
        </form>
      </div>
    </div>
  );
}

export default HomeView;
