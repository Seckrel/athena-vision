import styles from './home-view.module.scss';
import { clsx } from 'clsx';
import { useRef, useState } from 'react';

/* eslint-disable-next-line */
export interface HomeViewProps {}

export function HomeView(props: HomeViewProps) {
  const sliderRef = useRef(null);
  const [strengthSliderState, setStrengthSliderState] = useState('1');

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
        <button className={clsx(styles['enable-btn'], 'Typography-1')}>
          Enable
        </button>
        {/* Adjust Form */}
        <div>
          <form>
            <div className={styles['strength-slider-container']}>
              <label className="Typography-3">Strength: </label>
              <div className={styles['strength-slider-and-labels']}>
                <div className={styles['strength-slider-dot-wrapper']}>
                  <input
                    ref={sliderRef}
                    type="range"
                    className={styles['strength-slider']}
                    name="strength"
                    id="strength"
                    min={1}
                    max={3}
                    value={strengthSliderState}
                    onChange={(e) =>
                      setStrengthSliderState((_) => e.target.value)
                    }
                  />

                  <div className={styles['dots']}>
                    <div className={styles['dot']}>.</div>
                    <div className={styles['dot']}>.</div>
                    <div className={styles['dot']}>.</div>
                  </div>
                </div>

                <div className={styles['level-labels']}>
                  <span>Low</span>
                  <span>Mid</span>
                  <span>High</span>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default HomeView;
