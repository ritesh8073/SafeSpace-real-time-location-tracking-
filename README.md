# SafeSpace - Real-Time Location Tracking

SafeSpace is a real-time location tracking system designed to enhance safety and monitoring. It enables users to share their live location with trusted contacts, providing a reliable solution for emergency situations or general tracking needs.

## Features
- Real-time GPS location tracking
- Secure user authentication
- Location sharing with trusted contacts
- Interactive map interface
- Geofencing alerts
- Responsive and user-friendly UI

## Technologies Used
- Android (Kotlin/Java) for mobile application
- Firebase for real-time database and authentication
- Google Maps API for location tracking
- Node.js/Express (optional backend for advanced features)

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Android Studio
- A Firebase account with project setup
- Google Maps API key

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/ritesh8073/SafeSpace-real-time-location-tracking-.git
   cd SafeSpace-real-time-location-tracking-
   ```
2. Open the project in Android Studio.
3. Configure Firebase:
   - Add `google-services.json` to the `app/` directory.
   - Enable Firebase Authentication and Firestore Database.
4. Obtain a Google Maps API key and update `AndroidManifest.xml`.
5. Build and run the application on an emulator or physical device.

## How It Works
1. Users sign in securely using Firebase Authentication.
2. The app fetches and updates the user’s real-time location.
3. Location data is shared with selected contacts.
4. The map interface displays user movements dynamically.
5. Alerts are triggered if users enter or leave designated geofenced areas.

## Customization
- Modify UI components in `res/layout/`.
- Update tracking logic in `MainActivity.java`.
- Enhance security with encryption and access control.

## Future Enhancements
- SOS button for emergency alerts
- Offline tracking with local storage
- Advanced analytics for location history
- Integration with smart wearables

## License
This project is open-source and available for modification and distribution.

## Author
[ritesh8073](https://github.com/ritesh8073)

