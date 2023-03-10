# proteus
Core functionality of PROTEUS and utility

![PROTEUS Logo](proteus_logo.png)

The PROTEUS-HRI software system is a multi-modal system for underwater human-robot interaction, with an emphasis on reconfigurability and adapatility. It is the result of 6 years of research by Michael Fulton under the direction of Junaed Sattar at the University of Minnesota's Interactive Robotics and Vision Lab. You can find more information about the methods of communication, the design of PROTEUS, and the ACVS system in this org in Michael's thesis: https://michaelscottfulton.com/files/thesis_michael_fulton.pdf.

The code  is research code, meaning that there are known issues, known unimplemented behaviors, etc. As much as I would love to be able to develop PROTEUS to a point of true stability and ease of use, that's not the way that PhDs work, unfortunately. I hope that I've left sufficient in-code comments to make this code easy to understand, and that I've made the code easy to read. If you have difficulties with this code, please submit an issue or reach out to Michael personally.

The repositories which comprise the current PROTEUS system are:

- This repository, providing core functionality and the language server.
- [proteus_msgs](https://github.com/IRVLab/proteus_msgs), providing ROS messages, services, and actions.
- [proteus_diver_context](https://github.com/IRVLab/proteus_diver_context.git), which provides diver context tracking/
- [proteus_loco_oled](https://github.com/IRVLab/proteus_loco_oled), which provides digital display control for LoCO.
- [proteus_siren](https://github.com/IRVLab/proteus_siren), which provides sound-based AUV-to-human communcation.
- [proteus_hreye](https://github.com/IRVLab/proteus_hreye), which provides light-based AUV-to-human communication.
- [proteus_rcvm_loco](https://github.com/IRVLab/proteus_rcvm_loco), which provides motion-based AUV-to-human communication for LOCO.
- [proteus_rcvm_aqua](https://github.com/IRVLab/proteus_rcvm_aqua), which provides motion-based AUV-to-human communication for Aqua.
- [proteus_acvs](https://github.com/IRVLab/proteus_acvs), which provides Autonomous Communication Vector Selection: an adaptive form of AUV-to-human communication using all five of the vectors from other packages.

This code is all released under the GPLv3, meaning that you are free to use it, but any meaningiful changes you make must be re-released under the GPLv3. Please submit such changes as pull requests to the appropriate repositories, and Michael will merge them whenever possible.

