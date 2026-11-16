#
# Copyright (c) 2014-2024 Key4hep-Project.
#
# This file is part of Key4hep.
# See https://key4hep.github.io/key4hep-doc/ for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# HitPF (k4PFHitML, https://github.com/key4hep/k4PFHitML): hit-based ML particle flow,
# run on the EDM4hep collections produced by the Marlin chain. Loaded by
# CLDReconstruction.py --enableHitPF after the LCIO<->EDM4hep converters are assigned.
#
from Gaudi.Configuration import INFO
from Configurables import PFHitML

# models published at https://key4hep.web.cern.ch/testFiles/k4PFHitML/
_models = reco_args.hitpfModelDir

HitPF = PFHitML(
    "PFHitML",
    ClusteringModelPath=f"{_models}/clustering_paper.onnx",
    NeutralModelPath=f"{_models}/energy_correction_paper_neutral.onnx",
    ChargedModelPath=f"{_models}/energy_correction_paper_charged_pid.onnx",
    GeoSvcName=geoservice.name(),
    # CLD preset from k4PFHitML options/PerformMLPF.py
    EcalBarrelHits=["ECALBarrel"],
    EcalEndcapHits=["ECALEndcap"],
    HcalBarrelHits=["HCALBarrel"],
    HcalEndcapHits=["HCALEndcap"],
    HcalOtherHits=["HCALOther"],
    MuonHits=["MUON"],
    Tracks=["SiTracks_Refitted"],
    MCParticles=["MCParticles"],
    CalohitMCTruthLink=["CalohitMCTruthLink"],
    SiTracksMCTruthLink=["SiTracksMCTruthLink"],
    TruthBarrelRadius=2150.0,
    TruthNBarrelSides=12,
    TruthEndcapZ=2307.0,
    OutputLevel=INFO,
)

HitPFSequence = [HitPF]
