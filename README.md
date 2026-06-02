# Awesome Video Scene Parsing

<div align="center">
  <img src="https://img.shields.io/badge/Awesome-VSP-brightgreen?style=for-the-badge" alt="Awesome VSP">
  <img src="https://img.shields.io/badge/Papers-56%2B-blue?style=for-the-badge" alt="Papers">
  <img src="https://img.shields.io/badge/Code-21%2B-yellow?style=for-the-badge" alt="Code">
  <img src="https://img.shields.io/badge/Last%20Updated-June%202026-red?style=for-the-badge" alt="Last Updated">
</div>

## About This Repository

This repository is a companion index for the survey **A Comprehensive Survey on Video Scene Parsing: Advances, Challenges, and Prospects**. Its main purpose is simple: provide quick paper/code/project links for representative methods discussed in the survey.

Video Scene Parsing (VSP) covers video semantic segmentation, video instance segmentation, video panoptic segmentation, video tracking and segmentation, and open-vocabulary video segmentation. The list below follows that task structure so readers can move from a survey paragraph to the corresponding method quickly.

## Repository Statistics

| Area | Entries |
| :--- | :---: |
| Video Semantic Segmentation | 14 |
| Video Instance Segmentation | 16 |
| Video Panoptic Segmentation | 8 |
| Video Tracking & Segmentation | 9 |
| Open-Vocabulary Video Segmentation | 5 |
| Unified / Universal Video Segmentation | 3 |
| Emerging Directions | 1 |
| **Total** | **56** |

## Contents

- [Video Semantic Segmentation](#video-semantic-segmentation)
- [Video Instance Segmentation](#video-instance-segmentation)
- [Video Panoptic Segmentation](#video-panoptic-segmentation)
- [Video Tracking & Segmentation](#video-tracking-and-segmentation)
- [Open-Vocabulary Video Segmentation](#open-vocabulary-video-segmentation)
- [Unified / Universal Video Segmentation](#unified-universal-video-segmentation)
- [Emerging Directions](#emerging-directions)
- [Datasets](#datasets)
- [Contributing](#contributing)
- [Citation](#citation)

## Papers / Projects

### Video Semantic Segmentation

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2016 | **Clockwork** | [Clockwork ConvNets for Video Semantic Segmentation](https://scholar.google.com/scholar?q=Clockwork+ConvNets+for+Video+Semantic+Segmentation) | NA | Real-time, Feature reuse |
| 2017 | **NetWarp** | [Semantic Video CNNs Through Representation Warping](https://scholar.google.com/scholar?q=Semantic+Video+CNNs+Through+Representation+Warping) | NA | Flow, Feature propagation |
| 2017 | **PEARL** | [Video Scene Parsing with Predictive Feature Learning](https://scholar.google.com/scholar?q=Video+Scene+Parsing+with+Predictive+Feature+Learning) | NA | Flow, Prediction |
| 2018 | **Accel** | [Accel: A Corrective Fusion Network for Efficient Semantic Segmentation on Video](https://scholar.google.com/scholar?q=Accel+A+Corrective+Fusion+Network+for+Efficient+Semantic+Segmentation+on+Video) | NA | Flow, Efficiency |
| 2018 | **GCRF** | [Deep Spatio-Temporal Random Fields for Efficient Video Segmentation](https://scholar.google.com/scholar?q=Deep+Spatio-Temporal+Random+Fields+for+Efficient+Video+Segmentation) | NA | Flow, CRF |
| 2020 | **Naive-Student** | [Naive-Student: Leveraging Semi-Supervised Learning in Video Sequences for Urban Scene Segmentation](https://scholar.google.com/scholar?q=Naive-Student+Leveraging+Semi-Supervised+Learning+in+Video+Sequences+for+Urban+Scene+Segmentation) | NA | Semi-supervised, Pseudo labels |
| 2020 | **TDNet** | [Temporally Distributed Networks for Fast Video Semantic Segmentation](https://scholar.google.com/scholar?q=Temporally+Distributed+Networks+for+Fast+Video+Semantic+Segmentation) | NA | Attention, Real-time |
| 2022 | **CFFM** | [Coarse-to-Fine Feature Mining for Video Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Sun_Coarse-To-Fine_Feature_Mining_for_Video_Semantic_Segmentation_CVPR_2022_paper.html) | [Code](https://github.com/GuoleiSun/VSS-CFFM) | Attention, Temporal context |
| 2022 | **MRCFA** | [Mining Relations Among Cross-Frame Affinities for Video Semantic Segmentation](https://scholar.google.com/scholar?q=Mining+Relations+Among+Cross-Frame+Affinities+for+Video+Semantic+Segmentation) | NA | Attention, Affinity |
| 2023 | **MPVSS** | [Mask Propagation for Efficient Video Semantic Segmentation](https://scholar.google.com/scholar?q=Mask+Propagation+for+Efficient+Video+Semantic+Segmentation) | NA | Mask propagation, Efficiency |
| 2023 | **SSLTM** | [Simultaneously Short- and Long-Term Temporal Modeling for Semi-Supervised Video Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Lao_Simultaneously_Short-_and_Long-Term_Temporal_Modeling_for_Semi-Supervised_Video_Semantic_Segmentation_CVPR_2023_paper.html) | NA | Semi-supervised, Long-term |
| 2024 | **CFFM++** | [Learning Local and Global Temporal Contexts for Video Semantic Segmentation](https://scholar.google.com/scholar?q=Learning+Local+and+Global+Temporal+Contexts+for+Video+Semantic+Segmentation) | [Code](https://github.com/GuoleiSun/VSS-CFFM) | Attention, Temporal context |
| 2024 | **VPSeg** | [Vanishing-Point-Guided Video Semantic Segmentation of Driving Scenes](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_Vanishing-Point-Guided_Video_Semantic_Segmentation_of_Driving_Scenes_CVPR_2024_paper.html) | [Code](https://github.com/Daniel-Guo/VPSeg) | Transformer, Geometry |
| 2025 | **TV3S** | [Exploiting Temporal State Space Sharing for Video Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Hesham_Exploiting_Temporal_State_Space_Sharing_for_Video_Semantic_Segmentation_CVPR_2025_paper.html) | NA | Mamba, State space |

### Video Instance Segmentation

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2019 | **MaskTrack R-CNN** | [Video Instance Segmentation](https://openaccess.thecvf.com/content_ICCV_2019/html/Yang_Video_Instance_Segmentation_ICCV_2019_paper.html) | NA | Tracking-by-detection, Baseline |
| 2020 | **MaskProp** | [Classifying Segmenting and Tracking Object Instances in Video with Mask Propagation](https://openaccess.thecvf.com/content_CVPR_2020/html/Bertasius_Classifying_Segmenting_and_Tracking_Object_Instances_in_Video_With_Mask_Propagation_CVPR_2020_paper.html) | NA | Mask propagation, Tracking |
| 2020 | **STEm-Seg** | [STEm-Seg: Spatio-temporal Embeddings for Instance Segmentation in Videos](https://scholar.google.com/scholar?q=STEm-Seg+Spatio-temporal+Embeddings+for+Instance+Segmentation+in+Videos) | NA | Embedding, Clip-level |
| 2021 | **CrossVIS** | [Crossover Learning for Fast Online Video Instance Segmentation](https://openaccess.thecvf.com/content/ICCV2021/html/Yang_Crossover_Learning_for_Fast_Online_Video_Instance_Segmentation_ICCV_2021_paper.html) | [Code](https://github.com/hustvl/CrossVIS) | Online, Dynamic convolution |
| 2021 | **IFC** | [Video Instance Segmentation Using Inter-Frame Communication Transformers](https://scholar.google.com/scholar?q=Video+Instance+Segmentation+Using+Inter-Frame+Communication+Transformers) | NA | Transformer, Inter-frame communication |
| 2021 | **VisTR** | [End-to-End Video Instance Segmentation with Transformers](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_End-to-End_Video_Instance_Segmentation_With_Transformers_CVPR_2021_paper.html) | [Code](https://github.com/Epiphqny/VisTR) | Transformer, Set prediction |
| 2022 | **IDOL** | [In Defense of Online Models for Video Instance Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/6895_ECCV_2022_paper.php) | NA | Online, Contrastive learning |
| 2022 | **MinVIS** | [MinVIS: A Minimal Video Instance Segmentation Framework without Video-Based Training](https://proceedings.neurips.cc/paper_files/paper/2022/hash/5946db33de276c90b3438224d2aaa2aa-Abstract-Conference.html) | [Code](https://github.com/NVlabs/MinVIS) | Transformer, Minimal training |
| 2022 | **SeqFormer** | [SeqFormer: Sequential Transformer for Video Instance Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/4669_ECCV_2022_paper.php) | [Code](https://github.com/wjf5203/SeqFormer) | Transformer, Query |
| 2022 | **TeViT** | [Temporally Efficient Vision Transformer for Video Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Temporally_Efficient_Vision_Transformer_for_Video_Instance_Segmentation_CVPR_2022_paper.html) | NA | Transformer, Efficiency |
| 2023 | **CTVIS** | [CTVIS: Consistent Training for Online Video Instance Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Ying_CTVIS_Consistent_Training_for_Online_Video_Instance_Segmentation_ICCV_2023_paper.html) | [Code](https://github.com/KainingYing/CTVIS) | Contrastive memory, Online |
| 2023 | **DVIS** | [Decoupled Video Instance Segmentation Framework](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_DVIS_Decoupled_Video_Instance_Segmentation_Framework_ICCV_2023_paper.html) | [Code](https://github.com/zhang-tao-whu/DVIS) | Decoupled, Transformer |
| 2023 | **GenVIS** | [A Generalized Framework for Video Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Heo_A_Generalized_Framework_for_Video_Instance_Segmentation_CVPR_2023_paper.html) | [Code](https://github.com/haochenheheda/GenVIS) | Transformer, Generalized training |
| 2023 | **VideoCutLER** | [VideoCutLER: Surprisingly Simple Unsupervised Video Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_VideoCutLER_Surprisingly_Simple_Unsupervised_Video_Instance_Segmentation_CVPR_2023_paper.html) | NA | Unsupervised, DINO |
| 2024 | **OV2Seg+** | [OV-VIS: Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=OV-VIS+Open-Vocabulary+Video+Instance+Segmentation) | NA | Open vocabulary, VLM |
| 2024 | **OVFormer** | [Unified Embedding Alignment for Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=Unified+Embedding+Alignment+for+Open-Vocabulary+Video+Instance+Segmentation) | NA | Open vocabulary, Alignment |

### Video Panoptic Segmentation

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2020 | **Panoptic-DeepLab** | [Panoptic-DeepLab: A Simple Strong and Fast Baseline for Bottom-Up Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Cheng_Panoptic-DeepLab_A_Simple_Strong_and_Fast_Baseline_for_Bottom-Up_Panoptic_Segmentation_CVPR_2020_paper.html) | [Code](https://github.com/bowenc0221/panoptic-deeplab) | Dual branch, Bottom-up |
| 2020 | **ViP-DeepLab** | [ViP-DeepLab: Learning Visual Perception with Depth-aware Video Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Qiao_ViP-DeepLab_Learning_Visual_Perception_With_Depth-Aware_Video_Panoptic_Segmentation_CVPR_2020_paper.html) | NA | Depth-aware, 3D |
| 2020 | **VPSNet** | [Video Panoptic Segmentation](https://openaccess.thecvf.com/content_CVPR_2020/html/Kim_Video_Panoptic_Segmentation_CVPR_2020_paper.html) | NA | Dual branch, VPS |
| 2022 | **PolyphonicFormer** | [PolyphonicFormer: Unified Query Learning for Depth-aware Video Panoptic Segmentation](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/641_ECCV_2022_paper.php) | [Code](https://github.com/HarborYuan/PolyphonicFormer) | Query, Depth-aware |
| 2022 | **Slot-VPS** | [Slot-VPS: Object-Centric Representation Learning for Video Panoptic Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Zhou_Slot-VPS_Object-Centric_Representation_Learning_for_Video_Panoptic_Segmentation_CVPR_2022_paper.html) | NA | Object-centric, Slots |
| 2022 | **Video K-Net** | [Video K-Net: A Simple Strong and Unified Baseline for Video Segmentation](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Video_K-Net_A_Simple_Strong_and_Unified_Baseline_for_Video_Segmentation_CVPR_2022_paper.html) | [Code](https://github.com/lxtGH/Video-K-Net) | Query, Unified |
| 2023 | **Tube-Link** | [Tube-Link: A Flexible Cross Tube Framework for Universal Video Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Tube-Link_A_Flexible_Cross_Tube_Framework_for_Universal_Video_Segmentation_ICCV_2023_paper.html) | [Code](https://github.com/lxtGH/Tube-Link) | Tube, Universal segmentation |
| 2025 | **CAVIS** | [CAVIS: Context-Aware Video Instance Segmentation](https://scholar.google.com/scholar?q=CAVIS+Context-Aware+Video+Instance+Segmentation) | NA | Context, Association |

### Video Tracking & Segmentation

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2019 | **Track R-CNN** | [MOTS: Multi-Object Tracking and Segmentation](https://openaccess.thecvf.com/content_CVPR_2019/html/Voigtlaender_MOTS_Multi-Object_Tracking_and_Segmentation_CVPR_2019_paper.html) | NA | Tracking-by-detection, MOTS |
| 2020 | **PointTrack** | [Segment as Points for Efficient Online Multi-Object Tracking and Segmentation](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/309_ECCV_2020_paper.php) | [Code](https://github.com/detectRecog/PointTrack) | Point-based, Online |
| 2021 | **ASB** | [Assignment-Space-Based Multi-Object Tracking and Segmentation](https://openaccess.thecvf.com/content/ICCV2021/html/Choudhuri_Assignment-Space-Based_Multi-Object_Tracking_and_Segmentation_ICCV_2021_paper.html) | NA | Assignment, Optimization |
| 2022 | **MPNTrackSeg** | [Multi-Object Tracking and Segmentation via Neural Message Passing](https://scholar.google.com/scholar?q=Multi-Object+Tracking+and+Segmentation+via+Neural+Message+Passing) | NA | Graph, Message passing |
| 2023 | **DEVA** | [Tracking Anything with Decoupled Video Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Cheng_Tracking_Anything_With_Decoupled_Video_Segmentation_ICCV_2023_paper.html) | [Code](https://github.com/hkchengrex/Tracking-Anything-with-DEVA) | Decoupled, Foundation model |
| 2023 | **MITS** | [Integrating Boxes and Masks: A Multi-Object Framework for Unified Visual Tracking and Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Xu_Integrating_Boxes_and_Masks_A_Multi-Object_Framework_for_Unified_Visual_Tracking_ICCV_2023_paper.html) | [Code](https://github.com/yoxu515/MITS) | Transformer, Boxes and masks |
| 2023 | **SAM-PT** | [Segment Anything Meets Point Tracking](https://arxiv.org/abs/2307.01197) | [Code](https://github.com/SysCV/sam-pt) | SAM, Point tracking |
| 2023 | **SAM-Track** | [Segment and Track Anything](https://arxiv.org/abs/2305.06558) | [Code](https://github.com/z-x-yang/Segment-and-Track-Anything) | SAM, Interactive tracking |
| 2024 | **SAM 2** | [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) | [Code](https://github.com/facebookresearch/segment-anything-2) / [Project](https://sam2.metademolab.com/) | Foundation model, Promptable segmentation |

### Open-Vocabulary Video Segmentation

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2023 | **ODISE** | [Open-Vocabulary Panoptic Segmentation with Text-to-Image Diffusion Models](https://openaccess.thecvf.com/content/CVPR2023/html/Xu_Open-Vocabulary_Panoptic_Segmentation_With_Text-to-Image_Diffusion_Models_CVPR_2023_paper.html) | [Code](https://github.com/NVlabs/ODISE) | Open vocabulary, Diffusion |
| 2024 | **OV2Seg+** | [OV-VIS: Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=OV-VIS+Open-Vocabulary+Video+Instance+Segmentation) | NA | Open vocabulary, VIS |
| 2024 | **OVFormer** | [Unified Embedding Alignment for Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=Unified+Embedding+Alignment+for+Open-Vocabulary+Video+Instance+Segmentation) | NA | Open vocabulary, VIS |
| 2025 | **CLIP-VIS** | [CLIP-VIS: Adapting CLIP for Open-Vocabulary Video Instance Segmentation](https://scholar.google.com/scholar?q=CLIP-VIS+Adapting+CLIP+for+Open-Vocabulary+Video+Instance+Segmentation) | NA | Open vocabulary, CLIP |
| 2025 | **OV2VSS** | [Towards Open-Vocabulary Video Semantic Segmentation](https://scholar.google.com/scholar?q=Towards+Open-Vocabulary+Video+Semantic+Segmentation) | NA | Open vocabulary, VSS |

### Unified / Universal Video Segmentation

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2023 | **BURST** | [A Unified Benchmark for Multi-Object Tracking and Segmentation](https://scholar.google.com/scholar?q=BURST+A+Unified+Benchmark+for+Multi-Object+Tracking+and+Segmentation) | NA | Unified benchmark, Tracking |
| 2024 | **OMG-Seg** | [OMG-Seg: Is One Model Good Enough for All Segmentation?](https://scholar.google.com/scholar?q=OMG-Seg+Is+One+Model+Good+Enough+for+All+Segmentation) | NA | Unified model, Segmentation |
| 2025 | **DVIS++** | [DVIS++: Improved Decoupled Framework for Universal Video Segmentation](https://scholar.google.com/scholar?q=DVIS%2B%2B+Improved+Decoupled+Framework+for+Universal+Video+Segmentation) | NA | Universal video segmentation, Decoupled |

### Emerging Directions

| Year | Method | Paper | Resources | Tags |
| :---: | :--- | :--- | :---: | :--- |
| 2024 | **VideoSAM** | [VideoSAM: Open-World Video Segmentation](https://scholar.google.com/scholar?q=VideoSAM+Open-World+Video+Segmentation) | NA | Open-world, Foundation model |

## Datasets

| Dataset | Main Use | Link |
| :--- | :--- | :---: |
| Cityscapes | VSS / VPS driving scenes | [Project](https://www.cityscapes-dataset.com/) |
| VSPW | Large-scale VSS | [Project](https://www.vspwdataset.com/) |
| YouTube-VIS | VIS | [Project](https://youtube-vos.org/dataset/vis/) |
| OVIS | Occluded VIS | [Project](https://songbai.site/ovis/) |
| KITTI-MOTS | VTS / MOTS | [Project](https://www.vision.rwth-aachen.de/page/mots) |
| VIPSeg | VPS / long-tail video scene parsing | [Project](https://github.com/VIPSeg-Dataset/VIPSeg-Dataset) |
| LV-VIS | Open-vocabulary VIS | [Project](https://github.com/haochenheheda/LVVIS) |

## Contributing

Pull requests are welcome. The preferred workflow is to edit `data/papers.csv` and regenerate the README:

```bash
python3 scripts/generate_readme.py
```

Please include at least the method name, year, task, paper link, and code/project link when available. Use `NA` for unknown links.

## Citation

If this repository helps your work, please consider citing the companion survey once the final bibliographic information is available.
