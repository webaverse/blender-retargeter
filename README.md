# Easy Retargeting Plugin for Blender

This repo isolates the retargeting module from [Rokoko's Blender Plugin](https://github.com/Rokoko/rokoko-studio-live-blender) with none of the other cruft or frills.

## Retargeting
In order to retarget an animation in Blender you will need to do the following:

- Open the Retargeting panel

  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/47029758599/original/gt30hHJ2JCfKDmmALDxjffiHbYjqFMQFmg.png"/>

- Select an armature with an animation as the source armature, select an armature that should receive the animation as the target armature and then press "Build Bone List"

  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/47029758649/original/AuSYaHVCMTAQmTYRX8JHohflx4B6tu7EVQ.png"/>

- Check if the bones got filled in correctly and fix any incorrect or missing bones

  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/47029758669/original/O_kTjk6qEKnNr_jOmvMXa2OI5d561ttBqA.png"/>

- Select "Auto Scale" if the armatures differ in size or resize them manually
- In "Use Pose:" select the pose that should be used for retargeting
- Important: Make sure that both armature are in the same pose for correct retargeting
- Press "Retarget Animation"
- Done!

   [<img src="https://img.youtube.com/vi/Od8Ecr70A4Q/maxresdefault.jpg" width="50%">](https://youtu.be/Od8Ecr70A4Q)
