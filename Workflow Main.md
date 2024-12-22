```mermaid
graph TD
    %% Part A: Dataset Generation
    subgraph PartA ["Part A: Dataset<br/>Characteristics<br/>"]
        A1["Script: Try2"] --> |"Creates Images"| A2["Folder:<br/>seamount_images_equal_tiles"]
        A1 --> |"Creates Images"| A3["Folder:<br/>no_seamount_images_equal_tiles"]
        A4["Script: exploratory_data_analysis"] --> |"Analyzes"| A2
        A4 --> |"Analyzes"| A3

        A5["Script: Try5"] --> |"Creates Images"| A6["Folder:<br/>seamounts_galore"]
        A7["Script: Try6"] --> |"Creates Images"| A8["Folder:<br/>no_seamounts_galore"]
    end

    %% Part B: Baseline Model
    subgraph PartB ["Part B: BaselineModel"]
        A6 --> |"Copied to"| B1["Folder: dataset_for_galore_vol_1_1/<br/>with_seamount"]
        A8 --> |"Copied to"| B2["Folder: dataset_for_galore_vol_1_1/<br/>without_seamount"]

        B3["Script: baseline_model"] --> |"Uses"| B1
        B3 --> |"Uses"| B2
        B4["Script: alt_baseline_model"] --> |"Uses"| B1
        B4 --> |"Uses"| B2

        B1 --> |"Manually Sorted"| B5["Folder: dataset_for_galore_vol_1_1/<br/>with_seamount_manual1"]
        B2 --> |"Manually Sorted"| B6["Folder: dataset_for_galore_vol_1_1/<br/>without_seamount_manual1"]
    end

    %% Part C: Model
    subgraph PartC ["Part C: Model"]
        B5 --> |"Copied to"| C1["Folder: data_241208"]
        B6 --> |"Copied to"| C1

        C2["Script: baseline_model_galore_vol_1_1"] --> |"Processes and Evaluates"| C1
    end

