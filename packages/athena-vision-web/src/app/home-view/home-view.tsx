import styles from './home-view.module.scss';
import { clsx } from 'clsx';
import { useState, ChangeEvent } from 'react';

/* eslint-disable-next-line */
export interface HomeViewProps {}

export function HomeView(props: HomeViewProps) {
  const [strengthState, setStrengthState] = useState('1');

  const onStrengthChange = (e: ChangeEvent<HTMLInputElement>) => {
    setStrengthState((_) => e.target.value);
  };

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

        {/* <div className={styles['power-btn-container']}> */}
        <div className={styles['power-switch']}>
          <input type="checkbox" />
          <div className={styles['button']}>
            <svg className={styles['power-off']}>
              <use xlinkHref="#line" className={styles['line']} />
              <use xlinkHref="#circle" className={styles['circle']} />
            </svg>
            <svg className={styles['power-on']}>
              <use xlinkHref="#line" className={styles['line']} />
              <use xlinkHref="#circle" className={styles['line']} />
            </svg>
          </div>
        </div>

        {/* <!-- SVG --> */}
        <svg xmlns="http://www.w3.org/2000/svg" style={{ display: 'none' }}>
          <symbol
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 150 150"
            id="line"
          >
            <line x1="75" y1="34" x2="75" y2="58" />
          </symbol>
          <symbol
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 150 150"
            id="circle"
          >
            <circle cx="75" cy="80" r="35" />
          </symbol>
        </svg>
        {/* </div> */}

        {/* Adjust Form */}
        <form>
          <div className={styles['strength-slider-container']}>
            <h1 className={clsx(styles['filter-title'], 'Typography-5')}>
              Strength
            </h1>
            <div id={styles['strength-amount-slider']}>
              <input
                type="radio"
                name="strength-amount"
                id="low"
                value="0"
                checked={strengthState === '0'}
                onChange={onStrengthChange}
                required
              />
              <label htmlFor="low" data-strength-amount="Low"></label>
              <input
                type="radio"
                name="strength-amount"
                id="mid"
                value="1"
                checked={strengthState === '1'}
                onChange={onStrengthChange}
                required
              />
              <label htmlFor="mid" data-strength-amount="Mid"></label>
              <input
                type="radio"
                name="strength-amount"
                id="high"
                value="2"
                checked={strengthState === '2'}
                onChange={onStrengthChange}
                required
              />
              <label htmlFor="high" data-strength-amount="High"></label>
              <div id={styles['strength-amount-pos']}></div>
            </div>
          </div>

          <div className={styles['etone-switch-container']}>
            <h1 className={clsx(styles['filter-title'], 'Typography-5')}>
              Emotional Tone
            </h1>
            <div className={styles['etone-switch']}>
              <label className={styles['label']}>
                <div className={styles['toggle']}>
                  <input
                    className={styles['toggle-state']}
                    type="checkbox"
                    name="check"
                    value="check"
                  />
                  <div className={styles['indicator']}></div>
                </div>
              </label>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default HomeView;
