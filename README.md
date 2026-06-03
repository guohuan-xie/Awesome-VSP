# A Comprehensive Survey on Video Scene Parsing: Advances, Challenges, and Prospects

<div align="center">
  <img src="https://img.shields.io/badge/Awesome-VSP-brightgreen?style=for-the-badge" alt="Awesome VSP">
  <img src="https://img.shields.io/badge/Papers-56%2B-blue?style=for-the-badge" alt="Papers">
  <img src="https://img.shields.io/badge/Code%20%2F%20Project-40%2B-yellow?style=for-the-badge" alt="Code and Project">
  <img src="https://img.shields.io/badge/Last%20Updated-June%202026-red?style=for-the-badge" alt="Last Updated">
</div>

## About

This repository is a clean companion index for the survey **A Comprehensive Survey on Video Scene Parsing: Advances, Challenges, and Prospects**. It provides quick links to representative papers, code, project pages, and datasets mentioned in the survey.

Video Scene Parsing (VSP) covers **Video Semantic Segmentation (VSS)**, **Video Instance Segmentation (VIS)**, **Video Panoptic Segmentation (VPS)**, **Video Tracking & Segmentation (VTS)**, and **Open-Vocabulary Video Segmentation (OVVS)**.

## Repository Statistics

| Domain | Papers | Key Highlights |
| :--- | :---: | :--- |
| 🎞️ Video Semantic Segmentation | 14+ | Temporal consistency, feature propagation, efficient dense prediction |
| 🎭 Video Instance Segmentation | 16+ | Object masks, identity association, query-based tracking |
| 🧩 Video Panoptic Segmentation | 8+ | Unified thing/stuff parsing, tube masks, depth-aware parsing |
| 🎯 Video Tracking & Segmentation | 9+ | Long-horizon identity, point tracking, SAM-based propagation |
| 🌐 Open-Vocabulary Video Segmentation | 5+ | CLIP/VLM alignment, novel classes, open-world recognition |
| 🧠 Unified Video Segmentation | 3+ | One-model parsing, universal video segmentation, shared mask queries |
| 🚀 Emerging Directions | 1+ | Foundation models, open-world VSP, scalable generalization |

## Contents

- [🎞️ Video Semantic Segmentation](#vss)
- [🎭 Video Instance Segmentation](#vis)
- [🧩 Video Panoptic Segmentation](#vps)
- [🎯 Video Tracking & Segmentation](#vts)
- [🌐 Open-Vocabulary Video Segmentation](#ovvs)
- [🧠 Unified / Universal Video Segmentation](#unified)
- [🚀 Emerging Directions](#emerging)
- [📊 Datasets](#datasets)

## Papers / Projects

<a id="vss"></a>

### 🎞️ Video Semantic Segmentation

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2016 | **Clockwork** | [Clockwork ConvNets for Video Semantic Segmentation](https://arxiv.org/abs/1608.03609) | NA |
| 2017 | **NetWarp** | [Semantic Video CNNs Through Representation Warping](https://arxiv.org/abs/1708.03088) | [💻 Code](https://github.com/raghudeep/netwarp_public) |
| 2017 | **PEARL** | [Video Scene Parsing with Predictive Feature Learning](https://openaccess.thecvf.com/content_iccv_2017/html/Jin_Video_Scene_Parsing_ICCV_2017_paper.html) | NA |
| 2018 | **Accel** | [Accel: A Corrective Fusion Network for Efficient Semantic Segmentation on Video](https://openaccess.thecvf.com/content_CVPR_2019/html/Jain_Accel_A_Corrective_Fusion_Network_for_Efficient_Semantic_Segmentation_on_CVPR_2019_paper.html) | [🏠 Project](https://www.samvitjain.com/accel/) |
| 2018 | **GCRF** | [Deep Spatio-Temporal Random Fields for Efficient Video Segmentation](https://arxiv.org/abs/1807.03148) | [🏠 Project](https://engineering.fb.com/publication/deep-spatio-temporal-random-fields-for-efficient-video-segmentation/) |
| 2020 | **Naive-Student** | [Naive-Student: Leveraging Semi-Supervised Learning in Video Sequences for Urban Scene Segmentation](https://arxiv.org/abs/2005.10266) | [🏠 Project](https://research.google/pubs/naive-student-leveraging-semi-supervised-learning-in-video-sequences-for-urban-scene-segmentation/) |
| 2020 | **TDNet** | [Temporally Distributed Networks for Fast Video Semantic Segmentation](https://arxiv.org/abs/2004.01800) | [💻 Code](https://github.com/feinanshan/TDNet) / [🏠 Project](http://cs-people.bu.edu/pinghu/TDNet/) |
| 2022 | **CFFM** | [Coarse-to-Fine Feature Mining for Video Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Sun_Coarse-To-Fine_Feature_Mining_for_Video_Semantic_Segmentation_CVPR_2022_paper.html) | [💻 Code](https://github.com/GuoleiSun/VSS-CFFM) |
| 2022 | **MRCFA** | [Mining Relations Among Cross-Frame Affinities for Video Semantic Segmentation](https://arxiv.org/abs/2207.10436) | [💻 Code](https://github.com/GuoleiSun/VSS-MRCFA) |
| 2023 | **MPVSS** | [Mask Propagation for Efficient Video Semantic Segmentation](https://arxiv.org/abs/2310.18954) | [💻 Code](https://github.com/ziplab/MPVSS) |
| 2023 | **SSLTM** | [Simultaneously Short- and Long-Term Temporal Modeling for Semi-Supervised Video Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Lao_Simultaneously_Short-_and_Long-Term_Temporal_Modeling_for_Semi-Supervised_Video_Semantic_Segmentation_CVPR_2023_paper.html) | NA |
| 2024 | **CFFM++** | [Learning Local and Global Temporal Contexts for Video Semantic Segmentation](https://scholar.google.com/scholar?q=Learning+Local+and+Global+Temporal+Contexts+for+Video+Semantic+Segmentation) | [💻 Code](https://github.com/GuoleiSun/VSS-CFFM) |
| 2024 | **VPSeg** | [Vanishing-Point-Guided Video Semantic Segmentation of Driving Scenes](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_Vanishing-Point-Guided_Video_Semantic_Segmentation_of_Driving_Scenes_CVPR_2024_paper.html) | [💻 Code](https://github.com/Daniel-Guo/VPSeg) |
| 2025 | **TV3S** | [Exploiting Temporal State Space Sharing for Video Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Hesham_Exploiting_Temporal_State_Space_Sharing_for_Video_Semantic_Segmentation_CVPR_2025_paper.html) | [💻 Code](https://github.com/Ashesham/TV3S) |

<a id="vis"></a>

### 🎭 Video Instance Segmentation

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2019 | **MaskTrack R-CNN** | [Video Instance Segmentation](https://openaccess.thecvf.com/content_ICCV_2019/html/Yang_Video_Instance_Segmentation_ICCV_2019_paper.html) | [💻 Code](https://github.com/youtubevos/MaskTrackRCNN) |
| 2020 | **MaskProp** | [Classifying Segmenting and Tracking Object Instances in Video with Mask Propagation](https://arxiv.org/abs/1912.04573) | [🏠 Project](https://gberta.github.io/maskprop/) |
| 2020 | **STEm-Seg** | [STEm-Seg: Spatio-temporal Embeddings for Instance Segmentation in Videos](https://arxiv.org/abs/2003.08429) | [💻 Code](https://github.com/sabarim/STEm-Seg) |
| 2021 | **CrossVIS** | [Crossover Learning for Fast Online Video Instance Segmentation](https://openaccess.thecvf.com/content/ICCV2021/html/Yang_Crossover_Learning_for_Fast_Online_Video_Instance_Segmentation_ICCV_2021_paper.html) | [💻 Code](https://github.com/hustvl/CrossVIS) |
| 2021 | **IFC** | [Video Instance Segmentation Using Inter-Frame Communication Transformers](https://arxiv.org/abs/2106.03299) | [💻 Code](https://github.com/sukjunhwang/IFC) |
| 2021 | **VisTR** | [End-to-End Video Instance Segmentation with Transformers](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_End-to-End_Video_Instance_Segmentation_With_Transformers_CVPR_2021_paper.html) | [💻 Code](https://github.com/Epiphqny/VisTR) |
| 2022 | **IDOL** | [In Defense of Online Models for Video Instance Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6895_ECCV_2022_paper.php) | [💻 Code](https://github.com/wjf5203/VNext) |
| 2022 | **MinVIS** | [MinVIS: A Minimal Video Instance Segmentation Framework without Video-Based Training](https://proceedings.neurips.cc/paper_files/paper/2022/hash/5946db33de276c90b3438224d2aaa2aa-Abstract-Conference.html) | [💻 Code](https://github.com/NVlabs/MinVIS) |
| 2022 | **SeqFormer** | [SeqFormer: Sequential Transformer for Video Instance Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4669_ECCV_2022_paper.php) | [💻 Code](https://github.com/wjf5203/SeqFormer) |
| 2022 | **TeViT** | [Temporally Efficient Vision Transformer for Video Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Temporally_Efficient_Vision_Transformer_for_Video_Instance_Segmentation_CVPR_2022_paper.html) | [💻 Code](https://github.com/hustvl/TeViT) |
| 2023 | **CTVIS** | [CTVIS: Consistent Training for Online Video Instance Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Ying_CTVIS_Consistent_Training_for_Online_Video_Instance_Segmentation_ICCV_2023_paper.html) | [💻 Code](https://github.com/KainingYing/CTVIS) |
| 2023 | **DVIS** | [Decoupled Video Instance Segmentation Framework](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_DVIS_Decoupled_Video_Instance_Segmentation_Framework_ICCV_2023_paper.html) | [💻 Code](https://github.com/zhang-tao-whu/DVIS) |
| 2023 | **GenVIS** | [A Generalized Framework for Video Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Heo_A_Generalized_Framework_for_Video_Instance_Segmentation_CVPR_2023_paper.html) | [💻 Code](https://github.com/haochenheheda/GenVIS) |
| 2023 | **VideoCutLER** | [VideoCutLER: Surprisingly Simple Unsupervised Video Instance Segmentation](https://arxiv.org/abs/2308.14710) | [💻 Code](https://github.com/facebookresearch/CutLER) |
| 2024 | **OV2Seg+** | [OV-VIS: Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=OV-VIS+Open-Vocabulary+Video+Instance+Segmentation) | [💻 Code](https://github.com/haochenheheda/LVVIS) |
| 2024 | **OVFormer** | [Unified Embedding Alignment for Open-Vocabulary Video Instance Segmentation](https://arxiv.org/abs/2407.07427) | [💻 Code](https://github.com/fanghaook/OVFormer) |

<a id="vps"></a>

### 🧩 Video Panoptic Segmentation

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2020 | **Panoptic-DeepLab** | [Panoptic-DeepLab: A Simple Strong and Fast Baseline for Bottom-Up Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Cheng_Panoptic-DeepLab_A_Simple_Strong_and_Fast_Baseline_for_Bottom-Up_Panoptic_Segmentation_CVPR_2020_paper.html) | [💻 Code](https://github.com/bowenc0221/panoptic-deeplab) |
| 2020 | **ViP-DeepLab** | [ViP-DeepLab: Learning Visual Perception with Depth-aware Video Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Qiao_ViP-DeepLab_Learning_Visual_Perception_With_Depth-Aware_Video_Panoptic_Segmentation_CVPR_2020_paper.html) | [💻 Code](https://github.com/google-research/deeplab2) / [🏠 Project](https://www.cs.jhu.edu/~syqiao/projects/vip_deeplab/) |
| 2020 | **VPSNet** | [Video Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Video_Panoptic_Segmentation_CVPR_2020_paper.html) | [💻 Code](https://github.com/mcahny/vps) / [🏠 Project](https://github.com/mcahny/vps) |
| 2022 | **PolyphonicFormer** | [PolyphonicFormer: Unified Query Learning for Depth-aware Video Panoptic Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/641_ECCV_2022_paper.php) | [💻 Code](https://github.com/HarborYuan/PolyphonicFormer) |
| 2022 | **Slot-VPS** | [Slot-VPS: Object-Centric Representation Learning for Video Panoptic Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Zhou_Slot-VPS_Object-Centric_Representation_Learning_for_Video_Panoptic_Segmentation_CVPR_2022_paper.html) | [💻 Code](https://github.com/SAITPublic/SlotVPS) |
| 2022 | **Video K-Net** | [Video K-Net: A Simple Strong and Unified Baseline for Video Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Video_K-Net_A_Simple_Strong_and_Unified_Baseline_for_Video_Segmentation_CVPR_2022_paper.html) | [💻 Code](https://github.com/lxtGH/Video-K-Net) |
| 2023 | **Tube-Link** | [Tube-Link: A Flexible Cross Tube Framework for Universal Video Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Tube-Link_A_Flexible_Cross_Tube_Framework_for_Universal_Video_Segmentation_ICCV_2023_paper.html) | [💻 Code](https://github.com/lxtGH/Tube-Link) |
| 2025 | **CAVIS** | [CAVIS: Context-Aware Video Instance Segmentation](https://arxiv.org/abs/2407.03010) | [💻 Code](https://github.com/Seung-Hun-Lee/CAVIS) |

<a id="vts"></a>

### 🎯 Video Tracking & Segmentation

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2019 | **Track R-CNN** | [MOTS: Multi-Object Tracking and Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Voigtlaender_MOTS_Multi-Object_Tracking_and_Segmentation_CVPR_2019_paper.html) | [🏠 Project](https://www.vision.rwth-aachen.de/page/mots) |
| 2020 | **PointTrack** | [Segment as Points for Efficient Online Multi-Object Tracking and Segmentation](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/309_ECCV_2020_paper.php) | [💻 Code](https://github.com/detectRecog/PointTrack) |
| 2021 | **ASB** | [Assignment-Space-Based Multi-Object Tracking and Segmentation](https://openaccess.thecvf.com/content/ICCV2021/html/Choudhuri_Assignment-Space-Based_Multi-Object_Tracking_and_Segmentation_ICCV_2021_paper.html) | [🏠 Project](https://anwesachoudhuri.github.io/Assignment-Space-based-MOTS/) |
| 2022 | **MPNTrackSeg** | [Multi-Object Tracking and Segmentation via Neural Message Passing](https://arxiv.org/abs/2207.07454) | [💻 Code](https://github.com/ocetintas/MPNTrackSeg) |
| 2023 | **DEVA** | [Tracking Anything with Decoupled Video Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Cheng_Tracking_Anything_With_Decoupled_Video_Segmentation_ICCV_2023_paper.html) | [💻 Code](https://github.com/hkchengrex/Tracking-Anything-with-DEVA) |
| 2023 | **MITS** | [Integrating Boxes and Masks: A Multi-Object Framework for Unified Visual Tracking and Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Xu_Integrating_Boxes_and_Masks_A_Multi-Object_Framework_for_Unified_Visual_Tracking_ICCV_2023_paper.html) | [💻 Code](https://github.com/yoxu515/MITS) |
| 2023 | **SAM-PT** | [Segment Anything Meets Point Tracking](https://arxiv.org/abs/2307.01197) | [💻 Code](https://github.com/SysCV/sam-pt) |
| 2023 | **SAM-Track** | [Segment and Track Anything](https://arxiv.org/abs/2305.06558) | [💻 Code](https://github.com/z-x-yang/Segment-and-Track-Anything) |
| 2024 | **SAM 2** | [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) | [💻 Code](https://github.com/facebookresearch/segment-anything-2) / [🏠 Project](https://sam2.metademolab.com/) |

<a id="ovvs"></a>

### 🌐 Open-Vocabulary Video Segmentation

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2023 | **ODISE** | [Open-Vocabulary Panoptic Segmentation with Text-to-Image Diffusion Models](https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Open-Vocabulary_Panoptic_Segmentation_With_Text-to-Image_Diffusion_Models_CVPR_2023_paper.html) | [💻 Code](https://github.com/NVlabs/ODISE) |
| 2024 | **OV2Seg+** | [OV-VIS: Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=OV-VIS+Open-Vocabulary+Video+Instance+Segmentation) | [💻 Code](https://github.com/haochenheheda/LVVIS) |
| 2024 | **OVFormer** | [Unified Embedding Alignment for Open-Vocabulary Video Instance Segmentation](https://arxiv.org/abs/2407.07427) | [💻 Code](https://github.com/fanghaook/OVFormer) |
| 2025 | **CLIP-VIS** | [CLIP-VIS: Adapting CLIP for Open-Vocabulary Video Instance Segmentation](https://arxiv.org/abs/2403.12455) | [💻 Code](https://github.com/zwq456/CLIP-VIS) |
| 2025 | **OV2VSS** | [Towards Open-Vocabulary Video Semantic Segmentation](https://arxiv.org/abs/2412.09329) | [💻 Code](https://github.com/AVC2-UESTC/OV2VSS) |

<a id="unified"></a>

### 🧠 Unified / Universal Video Segmentation

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2023 | **BURST** | [A Unified Benchmark for Multi-Object Tracking and Segmentation](https://arxiv.org/abs/2209.12118) | [💻 Code](https://github.com/Ali2500/BURST-benchmark) |
| 2024 | **OMG-Seg** | [OMG-Seg: Is One Model Good Enough for All Segmentation?](https://arxiv.org/abs/2401.10229) | [💻 Code](https://github.com/lxtGH/OMG-Seg) / [🏠 Project](https://lxtgh.github.io/project/omg_seg/) |
| 2025 | **DVIS++** | [DVIS++: Improved Decoupled Framework for Universal Video Segmentation](https://arxiv.org/abs/2312.13305) | [💻 Code](https://github.com/zhang-tao-whu/DVIS_Plus) |

<a id="emerging"></a>

### 🚀 Emerging Directions

| Year | Method | Paper | Resources |
| :---: | :--- | :--- | :---: |
| 2024 | **VideoSAM** | [VideoSAM: Open-World Video Segmentation](https://arxiv.org/abs/2410.08781) | NA |

<a id="datasets"></a>

## 📊 Datasets

| Dataset | Main Use | Link |
| :--- | :--- | :---: |
| 🏙️ Cityscapes | VSS / VPS driving scenes | [🏠 Project](https://www.cityscapes-dataset.com/) |
| 🎞️ VSPW | Large-scale VSS | [🏠 Project](https://www.vspwdataset.com/) |
| 🎭 YouTube-VIS | VIS | [🏠 Project](https://youtube-vos.org/dataset/vis/) |
| 🙈 OVIS | Occluded VIS | [🏠 Project](https://songbai.site/ovis/) |
| 🚗 KITTI-MOTS | VTS / MOTS | [🏠 Project](https://www.vision.rwth-aachen.de/page/mots) |
| 🧩 VIPSeg | VPS / long-tail video scene parsing | [🏠 Project](https://github.com/VIPSeg-Dataset/VIPSeg-Dataset) |
| 🌐 LV-VIS | Open-vocabulary VIS | [🏠 Project](https://github.com/haochenheheda/LVVIS) |

## Contributing

Pull requests are welcome. Please keep entries concise and use `NA` when an official code or project page is unavailable.

## Citation

If this repository helps your work, please consider citing the companion survey.

```bibtex
@article{xie2025comprehensive,
  title={A Comprehensive Survey on Video Scene Parsing: Advances, Challenges, and Prospects},
  author={Xie, Guohuan and Hesham, Syed Ariff Syed and Guo, Wenya and Li, Bing and Cheng, Ming-Ming and Sun, Guolei and Liu, Yun},
  journal={arXiv preprint arXiv:2506.13552},
  year={2025}
}
```
