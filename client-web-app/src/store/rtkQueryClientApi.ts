import { emptySplitApi as api } from "./emptyApi";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    startRecorder: build.query<StartRecorderApiResponse, StartRecorderApiArg>({
      query: () => ({ url: `/rest/start-data-recording` }),
    }),
    stopRecorder: build.query<StopRecorderApiResponse, StopRecorderApiArg>({
      query: () => ({ url: `/rest/stop-data-recording` }),
    }),
    isDataRecording: build.query<
      IsDataRecordingApiResponse,
      IsDataRecordingApiArg
    >({
      query: () => ({ url: `/rest/is-data-recording` }),
    }),
    innerVideoStream: build.query<
      InnerVideoStreamApiResponse,
      InnerVideoStreamApiArg
    >({
      query: () => ({ url: `/rest/inner-video-stream` }),
    }),
    outerVideoStream: build.query<
      OuterVideoStreamApiResponse,
      OuterVideoStreamApiArg
    >({
      query: () => ({ url: `/rest/outer-video-stream` }),
    }),
    systemHealthSensors: build.query<
      SystemHealthSensorsApiResponse,
      SystemHealthSensorsApiArg
    >({
      query: () => ({ url: `/rest/system-health-sensors` }),
    }),
    solarCharger: build.query<SolarChargerApiResponse, SolarChargerApiArg>({
      query: () => ({ url: `/rest/solar-charger` }),
    }),
    accelerometerGyroSensor: build.query<
      AccelerometerGyroSensorApiResponse,
      AccelerometerGyroSensorApiArg
    >({
      query: () => ({ url: `/rest/accelerometer-gyro-sensor` }),
    }),
    currentSensor: build.query<CurrentSensorApiResponse, CurrentSensorApiArg>({
      query: () => ({ url: `/rest/current-sensor` }),
    }),
    coolerStrength: build.query<
      CoolerStrengthApiResponse,
      CoolerStrengthApiArg
    >({
      query: () => ({ url: `/rest/cooler-strength` }),
    }),
    switchCoolerOff: build.query<
      SwitchCoolerOffApiResponse,
      SwitchCoolerOffApiArg
    >({
      query: () => ({ url: `/rest/switch-cooler-off` }),
    }),
    switchCoolerOn: build.query<
      SwitchCoolerOnApiResponse,
      SwitchCoolerOnApiArg
    >({
      query: () => ({ url: `/rest/switch-cooler-on` }),
    }),
    getAllLedStrengths: build.query<
      GetAllLedStrengthsApiResponse,
      GetAllLedStrengthsApiArg
    >({
      query: () => ({ url: `/rest/all-led-strengths` }),
    }),
    setAllLedStrengths: build.mutation<
      SetAllLedStrengthsApiResponse,
      SetAllLedStrengthsApiArg
    >({
      query: (queryArg) => ({
        url: `/rest/all-led-strengths`,
        method: "POST",
        params: { leds: queryArg.leds },
      }),
    }),
    ledStrength: build.query<LedStrengthApiResponse, LedStrengthApiArg>({
      query: (queryArg) => ({ url: `/rest/led-strength/${queryArg.ledId}` }),
    }),
    switchLedOff: build.query<SwitchLedOffApiResponse, SwitchLedOffApiArg>({
      query: (queryArg) => ({ url: `/rest/switch-led-off/${queryArg.ledId}` }),
    }),
    switchLedOn: build.query<SwitchLedOnApiResponse, SwitchLedOnApiArg>({
      query: (queryArg) => ({ url: `/rest/switch-led-on/${queryArg.ledId}` }),
    }),
    switchLedTo: build.query<SwitchLedToApiResponse, SwitchLedToApiArg>({
      query: (queryArg) => ({
        url: `/rest/dim-led-to/${queryArg.ledId}/${queryArg.nextStrength}`,
      }),
    }),
    pantiltOrientation: build.query<
      PantiltOrientationApiResponse,
      PantiltOrientationApiArg
    >({
      query: () => ({ url: `/rest/pantilt-orientation` }),
    }),
    panToMin: build.query<PanToMinApiResponse, PanToMinApiArg>({
      query: () => ({ url: `/rest/pan-to-min` }),
    }),
    panToMiddle: build.query<PanToMiddleApiResponse, PanToMiddleApiArg>({
      query: () => ({ url: `/rest/pan-to-middle` }),
    }),
    panToMax: build.query<PanToMaxApiResponse, PanToMaxApiArg>({
      query: () => ({ url: `/rest/pan-to-max` }),
    }),
    panBy: build.query<PanByApiResponse, PanByApiArg>({
      query: (queryArg) => ({ url: `/rest/pan-by/${queryArg.relativeangle}` }),
    }),
    tiltToMin: build.query<TiltToMinApiResponse, TiltToMinApiArg>({
      query: () => ({ url: `/rest/tilt-to-min` }),
    }),
    tiltToMiddle: build.query<TiltToMiddleApiResponse, TiltToMiddleApiArg>({
      query: () => ({ url: `/rest/tilt-to-middle` }),
    }),
    tiltToMax: build.query<TiltToMaxApiResponse, TiltToMaxApiArg>({
      query: () => ({ url: `/rest/tilt-to-max` }),
    }),
    tiltBy: build.query<TiltByApiResponse, TiltByApiArg>({
      query: (queryArg) => ({ url: `/rest/tilt-by/${queryArg.relativeangle}` }),
    }),
    readIndex: build.query<ReadIndexApiResponse, ReadIndexApiArg>({
      query: () => ({ url: `/` }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as rtkQueryClientApi };
export type StartRecorderApiResponse =
  /** status 200 Successful Response */ boolean;
export type StartRecorderApiArg = void;
export type StopRecorderApiResponse =
  /** status 200 Successful Response */ boolean;
export type StopRecorderApiArg = void;
export type IsDataRecordingApiResponse =
  /** status 200 Successful Response */ boolean;
export type IsDataRecordingApiArg = void;
export type InnerVideoStreamApiResponse = unknown;
export type InnerVideoStreamApiArg = void;
export type OuterVideoStreamApiResponse = unknown;
export type OuterVideoStreamApiArg = void;
export type SystemHealthSensorsApiResponse =
  /** status 200 Successful Response */ SystemHealthReading;
export type SystemHealthSensorsApiArg = void;
export type SolarChargerApiResponse =
  /** status 200 Successful Response */ SolarChargerReading;
export type SolarChargerApiArg = void;
export type AccelerometerGyroSensorApiResponse =
  /** status 200 Successful Response */ AccelerometerGyroSensorReading;
export type AccelerometerGyroSensorApiArg = void;
export type CurrentSensorApiResponse =
  /** status 200 Successful Response */ Ina219SensorReading;
export type CurrentSensorApiArg = void;
export type CoolerStrengthApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type CoolerStrengthApiArg = void;
export type SwitchCoolerOffApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type SwitchCoolerOffApiArg = void;
export type SwitchCoolerOnApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type SwitchCoolerOnApiArg = void;
export type GetAllLedStrengthsApiResponse =
  /** status 200 Successful Response */ PwmDevice[];
export type GetAllLedStrengthsApiArg = void;
export type SetAllLedStrengthsApiResponse =
  /** status 200 Successful Response */ PwmDevice[];
export type SetAllLedStrengthsApiArg = {
  leds?: any;
};
export type LedStrengthApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type LedStrengthApiArg = {
  ledId: number;
};
export type SwitchLedOffApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type SwitchLedOffApiArg = {
  ledId: number;
};
export type SwitchLedOnApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type SwitchLedOnApiArg = {
  ledId: number;
};
export type SwitchLedToApiResponse =
  /** status 200 Successful Response */ PwmDevice;
export type SwitchLedToApiArg = {
  ledId: number;
  nextStrength: number;
};
export type PantiltOrientationApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type PantiltOrientationApiArg = void;
export type PanToMinApiResponse = /** status 200 Successful Response */ PanTilt;
export type PanToMinApiArg = void;
export type PanToMiddleApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type PanToMiddleApiArg = void;
export type PanToMaxApiResponse = /** status 200 Successful Response */ PanTilt;
export type PanToMaxApiArg = void;
export type PanByApiResponse = /** status 200 Successful Response */ PanTilt;
export type PanByApiArg = {
  relativeangle: number;
};
export type TiltToMinApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type TiltToMinApiArg = void;
export type TiltToMiddleApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type TiltToMiddleApiArg = void;
export type TiltToMaxApiResponse =
  /** status 200 Successful Response */ PanTilt;
export type TiltToMaxApiArg = void;
export type TiltByApiResponse = /** status 200 Successful Response */ PanTilt;
export type TiltByApiArg = {
  relativeangle: number;
};
export type ReadIndexApiResponse = /** status 200 Successful Response */ any;
export type ReadIndexApiArg = void;
export type SystemHealthReading = {
  cpu_temp: number;
  cpu_usage: number;
};
export type SolarChargerReading = {
  power_good: number;
  charging: number;
};
export type AccelerometerGyroSensorReading = {
  acceleration: [number, number, number];
  gyro: [number, number, number];
};
export type Ina219SensorReading = {
  vin_plus_voltage: number;
  bus_voltage: number;
  shunt_voltage: number;
  current: number;
  powerCalc: number;
  powerRegister: number;
};
export type PwmDevice = {
  identifier?: number;
  strength?: number;
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type PanTilt = {
  pan?: number;
  tilt?: number;
};
export const {
  useStartRecorderQuery,
  useLazyStartRecorderQuery,
  useStopRecorderQuery,
  useLazyStopRecorderQuery,
  useIsDataRecordingQuery,
  useLazyIsDataRecordingQuery,
  useInnerVideoStreamQuery,
  useLazyInnerVideoStreamQuery,
  useOuterVideoStreamQuery,
  useLazyOuterVideoStreamQuery,
  useSystemHealthSensorsQuery,
  useLazySystemHealthSensorsQuery,
  useSolarChargerQuery,
  useLazySolarChargerQuery,
  useAccelerometerGyroSensorQuery,
  useLazyAccelerometerGyroSensorQuery,
  useCurrentSensorQuery,
  useLazyCurrentSensorQuery,
  useCoolerStrengthQuery,
  useLazyCoolerStrengthQuery,
  useSwitchCoolerOffQuery,
  useLazySwitchCoolerOffQuery,
  useSwitchCoolerOnQuery,
  useLazySwitchCoolerOnQuery,
  useGetAllLedStrengthsQuery,
  useLazyGetAllLedStrengthsQuery,
  useSetAllLedStrengthsMutation,
  useLedStrengthQuery,
  useLazyLedStrengthQuery,
  useSwitchLedOffQuery,
  useLazySwitchLedOffQuery,
  useSwitchLedOnQuery,
  useLazySwitchLedOnQuery,
  useSwitchLedToQuery,
  useLazySwitchLedToQuery,
  usePantiltOrientationQuery,
  useLazyPantiltOrientationQuery,
  usePanToMinQuery,
  useLazyPanToMinQuery,
  usePanToMiddleQuery,
  useLazyPanToMiddleQuery,
  usePanToMaxQuery,
  useLazyPanToMaxQuery,
  usePanByQuery,
  useLazyPanByQuery,
  useTiltToMinQuery,
  useLazyTiltToMinQuery,
  useTiltToMiddleQuery,
  useLazyTiltToMiddleQuery,
  useTiltToMaxQuery,
  useLazyTiltToMaxQuery,
  useTiltByQuery,
  useLazyTiltByQuery,
  useReadIndexQuery,
  useLazyReadIndexQuery,
} = injectedRtkApi;
