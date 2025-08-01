# Release History

## 1.1.1 (Unreleased)

### Features Added

### Breaking Changes

### Bugs Fixed

### Other Changes

## 1.1.0 (2025-07-18)

### Bugs Fixed

- Fixed an issue where the package version in operation user agent strings was always set to "unknown" instead of the actual package version. ([#39866](https://github.com/Azure/azure-sdk-for-python/pull/39866))

### Other Changes

- Python 3.9 is now the minimum supported version for this package.

## 1.0.4 (2024-06-11)

### Other Changes

- Bumped minimum dependency on `azure-core` to `>=1.28.0`.
- Added additional type validation for the `logs` parameter in the `upload` method to ensure that a string hasn't been passed in. ([#33976](https://github.com/Azure/azure-sdk-for-python/pull/33976))

## 1.0.3 (2023-11-07)

### Other Changes

- Add type validation for the `logs` parameter in the `upload` method. ([#32591](https://github.com/Azure/azure-sdk-for-python/pull/32591/))

## 1.0.2 (2023-06-15)

### Bugs Fixed

- Fixed issue preventing custom authentication policies or credential scopes to be passed to the client. ([#30739](https://github.com/Azure/azure-sdk-for-python/pull/30739/))

## 1.0.1 (2023-04-11)

### Bugs Fixed
  - Fixed an issue where log entry sizes were miscalculated when chunking. ([#29584](https://github.com/Azure/azure-sdk-for-python/pull/29584))

## 1.0.0 (2023-02-16)

### Features Added
  - Added new `on_error` parameter to the `upload` method to allow users to handle errors in their own way.
    - An `LogsUploadError` class was added to encapsulate information about the error. An instance of this class is passed to the `on_error` callback.
  - Added IO support for upload. Now IO streams can be passed in using the `logs` parameter. ([#28373](https://github.com/Azure/azure-sdk-for-python/pull/28373))

### Breaking Changes
  - Removed support for max_concurrency

### Other Changes
  - Removed `msrest` dependency.
  - Added requirement for `isodate>=0.6.0` (`isodate` was required by `msrest`).
  - Added requirement for `typing-extensions>=4.0.1`.

## 1.0.0b1 (2022-07-15)

  ## Features
  - Version (1.0.0b1) is the first preview of our efforts to create a user-friendly and Pythonic client library for Azure Monitor Ingestion.
    For more information about this, and preview releases of other Azure SDK libraries, please visit https://azure.github.io/azure-sdk/releases/latest/python.html.
  - Added `~azure.monitor.ingestion.LogsIngestionClient` to send logs to Azure Monitor along with `~azure.monitor.ingestion.aio.LogsIngestionClient`.
