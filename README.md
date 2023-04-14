# Video Size Add-on for Blender Sequencer

This add-on for Blender Sequencer allows you to easily set the output properties of your video or image sequence to match the dimensions of your input video. It adds a new menu item to the Sequencer menu, under "Add".

## Installation

1. Download the "change_to_video_size.py" file.
2. In Blender, open the Preferences window.
3. Click on the "Add-ons" tab.
4. Click the "Install" button at the top of the window.
5. Navigate to the "change_to_video_size.py" file and select it.
6. Check the box next to "Change to Video Size" in the list of add-ons to enable it.

## Usage

1. Import your video or image sequence into the Sequencer.
2. Select the strip that represents your video or image sequence.
3. Go to the Sequencer menu and click "Add" > "Change to Video Size".
4. In the pop-up window, choose the desired fit method from the dropdown menu:
    * "Fit": Fits the video to the output resolution while maintaining aspect ratio.
    * "Fill": Fills the output resolution with the video while maintaining aspect ratio.
    * "Stretch": Stretches the video to fit the output resolution, potentially distorting the aspect ratio.
    * "Change to Video Size": Sets the output resolution to match the dimensions of the video.
5. Click "OK" to apply the changes.

## Limitations

- This add-on only works with video and image sequences imported into the Sequencer. It does not work with other types of media or with media imported into other parts of Blender.
- This add-on does not perform any scaling or cropping of the video. It simply sets the output resolution to match the dimensions of the video, potentially leaving unused space around the video in the output.
